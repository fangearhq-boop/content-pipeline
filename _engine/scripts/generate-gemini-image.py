"""
Gemini Image Generator for FanGear HQ Content Pipeline
========================================================
Generates AI images from visual descriptions using the Google Gemini API.
Supports two modes:
  - base_only:  Clean background image (no text) for Canva text overlay workflow
  - complete:   Finished graphic with text/branding baked in (bypasses Canva)

Usage:
    # Base image for Canva workflow
    python generate-gemini-image.py \
        --prompt "A vibrant playground scene with diverse families enjoying a sunny day" \
        --dimensions 1200x675 \
        --mode base_only \
        --output ./parenting-content-2026-02-22/generated-images/story-1-x.png

    # Complete graphic with text
    python generate-gemini-image.py \
        --prompt "A social media graphic about childcare costs..." \
        --dimensions 1200x675 \
        --mode complete \
        --output ./parenting-content-2026-02-22/generated-images/story-1-x.png

    # Dry run (shows what would happen, no API call)
    python generate-gemini-image.py \
        --prompt "..." --dimensions 1200x675 --dry-run

    # Check current usage and spending
    python generate-gemini-image.py --budget

    # Override daily cap for this run (use with caution)
    python generate-gemini-image.py --prompt "..." --daily-cap 75

Environment:
    GEMINI_API_KEY       — Required. Your Google Gemini API key.
    GEMINI_DAILY_CAP     — Optional. Max images per day (default: 50).
    GEMINI_MONTHLY_WARN  — Optional. Monthly spend warning threshold in dollars (default: $25).

Dependencies:
    pip install google-genai Pillow
"""

import argparse
import io
import json
import os
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional, Tuple

try:
    from google import genai
    from google.genai import types
except ImportError:
    print("Error: google-genai package not installed.")
    print("Install with: pip install google-genai")
    sys.exit(1)

try:
    from PIL import Image
except ImportError:
    print("Error: Pillow package not installed.")
    print("Install with: pip install Pillow")
    sys.exit(1)


# ── Constants ────────────────────────────────────────────────

DEFAULT_MODEL = "gemini-2.5-flash-image"
HIGH_QUALITY_MODEL = "gemini-3-pro-image-preview"

# Aspect ratios mapped to the closest Gemini API option
# X/Twitter: 1200x675 = 1.778:1 ~ 16:9
# Facebook:  1200x630 = 1.905:1 ~ 16:9 (closest available)
DIMENSION_TO_ASPECT = {
    (1080, 1350): "4:5",   # Social media posts (all platforms — optimal mobile feed)
    (1200, 675): "16:9",   # Legacy X/Twitter landscape
    (1200, 630): "16:9",   # Article hero / Open Graph
    (1080, 1080): "1:1",   # Instagram square
    (1080, 1920): "9:16",  # Stories
    (1280, 720): "16:9",   # YouTube thumbnail
}

MAX_RETRIES = 3
RETRY_DELAY_SECONDS = 5


# ── Guardrails & Cost Tracking ──────────────────────────────

# Estimated cost per image by model (USD)
COST_PER_IMAGE = {
    "gemini-2.5-flash-image": 0.04,
    "gemini-3-pro-image-preview": 0.20,
}

# Default safety limits
DAILY_CAP_DEFAULT = 50        # Max images per calendar day
PER_RUN_CAP_DEFAULT = 20      # Max images per single script execution
MONTHLY_WARN_DEFAULT = 25.00  # Warn when monthly spend exceeds this (USD)

# Generation log lives next to this script
LOG_FILE = Path(__file__).parent / "gemini-generation-log.json"

# Per-run counter (resets each time the script starts)
_run_image_count = 0


def _load_log() -> list:
    """Load the generation log from disk."""
    if not LOG_FILE.exists():
        return []
    try:
        with open(LOG_FILE, "r") as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        return []


def _save_log(entries: list):
    """Save the generation log to disk."""
    try:
        LOG_FILE.parent.mkdir(parents=True, exist_ok=True)
        with open(LOG_FILE, "w") as f:
            json.dump(entries, f, indent=2)
    except IOError as e:
        print(f"  Warning: Could not save generation log: {e}")


def _log_generation(model: str, mode: str, dimensions: str, success: bool,
                    output_path: Optional[str] = None):
    """Record one generation attempt in the log."""
    cost = COST_PER_IMAGE.get(model, 0.10)  # fallback estimate for unknown models
    entry = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "model": model,
        "mode": mode,
        "dimensions": dimensions,
        "cost_estimate_usd": cost if success else 0.0,
        "success": success,
        "output_path": output_path,
    }
    log = _load_log()
    log.append(entry)
    _save_log(log)


def _get_today_str() -> str:
    """Get today's date string in UTC for matching log entries."""
    return datetime.now(timezone.utc).strftime("%Y-%m-%d")


def _count_today_images() -> int:
    """Count how many images were successfully generated today."""
    today = _get_today_str()
    log = _load_log()
    count = 0
    for entry in log:
        if entry.get("success") and entry.get("timestamp", "").startswith(today):
            count += 1
    return count


def _get_monthly_spend() -> float:
    """Calculate estimated spend for the current month."""
    month_prefix = datetime.now(timezone.utc).strftime("%Y-%m")
    log = _load_log()
    total = 0.0
    for entry in log:
        if entry.get("success") and entry.get("timestamp", "").startswith(month_prefix):
            total += entry.get("cost_estimate_usd", 0.0)
    return total


def _get_daily_cap() -> int:
    """Get the daily image cap from env var or default."""
    try:
        return int(os.environ.get("GEMINI_DAILY_CAP", DAILY_CAP_DEFAULT))
    except ValueError:
        return DAILY_CAP_DEFAULT


def _get_monthly_warn() -> float:
    """Get the monthly warning threshold from env var or default."""
    try:
        return float(os.environ.get("GEMINI_MONTHLY_WARN", MONTHLY_WARN_DEFAULT))
    except ValueError:
        return MONTHLY_WARN_DEFAULT


def check_guardrails(model: str, daily_cap_override: Optional[int] = None,
                     per_run_cap_override: Optional[int] = None) -> bool:
    """
    Check all spending guardrails before generating an image.
    Returns True if safe to proceed, False if blocked.
    Prints warnings/errors as needed.
    """
    global _run_image_count

    # 1. Per-run batch limit
    per_run_cap = per_run_cap_override or PER_RUN_CAP_DEFAULT
    if _run_image_count >= per_run_cap:
        print(f"\n  GUARDRAIL BLOCKED: Per-run limit reached ({_run_image_count}/{per_run_cap} images)")
        print(f"  This prevents runaway loops in a single execution.")
        print(f"  To increase: use --per-run-cap N")
        return False

    # 2. Daily cap
    daily_cap = daily_cap_override or _get_daily_cap()
    today_count = _count_today_images()
    if today_count >= daily_cap:
        print(f"\n  GUARDRAIL BLOCKED: Daily limit reached ({today_count}/{daily_cap} images today)")
        print(f"  This prevents accidental mass generation.")
        print(f"  To increase: set GEMINI_DAILY_CAP env var or use --daily-cap N")
        print(f"  To check usage: python generate-gemini-image.py --budget")
        return False

    # 3. Monthly spend warning (soft — warns but allows)
    monthly_spend = _get_monthly_spend()
    monthly_warn = _get_monthly_warn()
    cost_est = COST_PER_IMAGE.get(model, 0.10)
    if monthly_spend + cost_est > monthly_warn:
        print(f"\n  WARNING: Monthly spend will exceed ${monthly_warn:.2f} warning threshold")
        print(f"  Current month: ${monthly_spend:.2f} + this image ~${cost_est:.2f} = ${monthly_spend + cost_est:.2f}")
        print(f"  To adjust threshold: set GEMINI_MONTHLY_WARN env var")

    # 4. Show running counts
    remaining_today = daily_cap - today_count - 1
    remaining_run = per_run_cap - _run_image_count - 1
    print(f"  Guardrails: {today_count + 1}/{daily_cap} today | "
          f"{_run_image_count + 1}/{per_run_cap} this run | "
          f"~${monthly_spend + cost_est:.2f} this month")

    return True


def print_budget_report():
    """Print a detailed usage and spending report."""
    log = _load_log()
    today = _get_today_str()
    month_prefix = datetime.now(timezone.utc).strftime("%Y-%m")

    # Today's stats
    today_entries = [e for e in log if e.get("timestamp", "").startswith(today)]
    today_success = [e for e in today_entries if e.get("success")]
    today_failed = [e for e in today_entries if not e.get("success")]
    today_cost = sum(e.get("cost_estimate_usd", 0) for e in today_success)

    # This month's stats
    month_entries = [e for e in log if e.get("timestamp", "").startswith(month_prefix)]
    month_success = [e for e in month_entries if e.get("success")]
    month_cost = sum(e.get("cost_estimate_usd", 0) for e in month_success)

    # All time stats
    all_success = [e for e in log if e.get("success")]
    all_cost = sum(e.get("cost_estimate_usd", 0) for e in all_success)

    # Model breakdown for this month
    model_counts = {}
    for e in month_success:
        m = e.get("model", "unknown")
        model_counts[m] = model_counts.get(m, 0) + 1

    daily_cap = _get_daily_cap()
    monthly_warn = _get_monthly_warn()

    print("=" * 60)
    print("  GEMINI IMAGE GENERATION — USAGE REPORT")
    print("=" * 60)

    print(f"\n  TODAY ({today}):")
    print(f"    Images generated:  {len(today_success)}")
    print(f"    Failed attempts:   {len(today_failed)}")
    print(f"    Estimated cost:    ${today_cost:.2f}")
    print(f"    Daily cap:         {daily_cap} images")
    print(f"    Remaining today:   {max(0, daily_cap - len(today_success))} images")

    print(f"\n  THIS MONTH ({month_prefix}):")
    print(f"    Images generated:  {len(month_success)}")
    print(f"    Estimated cost:    ${month_cost:.2f}")
    print(f"    Warning threshold: ${monthly_warn:.2f}")
    if model_counts:
        print(f"    By model:")
        for m, c in sorted(model_counts.items()):
            cost = COST_PER_IMAGE.get(m, 0.10)
            print(f"      {m}: {c} images (~${c * cost:.2f})")

    print(f"\n  ALL TIME:")
    print(f"    Total images:      {len(all_success)}")
    print(f"    Total log entries: {len(log)}")
    print(f"    Estimated cost:    ${all_cost:.2f}")

    print(f"\n  GUARDRAIL SETTINGS:")
    print(f"    Daily cap:         {daily_cap} (env: GEMINI_DAILY_CAP)")
    print(f"    Per-run cap:       {PER_RUN_CAP_DEFAULT} (flag: --per-run-cap)")
    print(f"    Monthly warning:   ${monthly_warn:.2f} (env: GEMINI_MONTHLY_WARN)")

    # Cost reference
    print(f"\n  COST REFERENCE:")
    for m, c in sorted(COST_PER_IMAGE.items()):
        print(f"    {m}: ~${c:.2f}/image")
    print(f"    Typical day (8 stories x 2 platforms): "
          f"~${16 * COST_PER_IMAGE[DEFAULT_MODEL]:.2f} with {DEFAULT_MODEL}")

    print(f"\n  Log file: {LOG_FILE}")
    print("=" * 60)


# ── Core Generation ──────────────────────────────────────────

def _read_key_file() -> Optional[str]:
    """Read API key from a local .gemini-key file (never committed to git)."""
    # Check next to this script first, then engine root, then user home
    candidates = [
        Path(__file__).parent / ".gemini-key",
        Path(__file__).parent.parent / ".gemini-key",
        Path.home() / ".gemini-key",
    ]
    for kf in candidates:
        if kf.is_file():
            key = kf.read_text().strip()
            if key:
                return key
        elif kf.is_dir():
            # Windows sometimes creates a folder instead of a file —
            # look for a text file inside it
            for child in kf.iterdir():
                if child.is_file():
                    key = child.read_text().strip()
                    if key:
                        return key
    return None


def get_client() -> genai.Client:
    """Initialize the Gemini API client. Checks .gemini-key file first, then env var."""
    api_key = _read_key_file()
    if not api_key:
        api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        print("Error: Gemini API key not found.")
        print("Option 1: Create a .gemini-key file containing just the key:")
        print(f"          {Path(__file__).parent / '.gemini-key'}")
        print("Option 2: Set GEMINI_API_KEY environment variable")
        print("\nThe .gemini-key file is gitignored and never leaves your machine.")
        sys.exit(1)
    return genai.Client(api_key=api_key)


def get_aspect_ratio(width: int, height: int) -> str:
    """Determine the best Gemini aspect ratio for target dimensions."""
    exact = DIMENSION_TO_ASPECT.get((width, height))
    if exact:
        return exact

    # Calculate ratio and find closest match
    ratio = width / height
    options = {
        "1:1": 1.0,
        "4:3": 1.333,
        "3:2": 1.5,
        "16:9": 1.778,
        "21:9": 2.333,
        "3:4": 0.75,
        "2:3": 0.667,
        "9:16": 0.5625,
        "5:4": 1.25,
        "4:5": 0.8,
    }
    closest = min(options, key=lambda k: abs(options[k] - ratio))
    return closest


def get_image_size(model: str, width: int) -> Optional[str]:
    """Determine resolution tier. Only applies to gemini-3-pro-image-preview."""
    if model != HIGH_QUALITY_MODEL:
        return None  # gemini-2.5-flash-image ignores image_size

    if width <= 1024:
        return "1K"
    elif width <= 2048:
        return "2K"
    else:
        return "4K"


def build_prompt(user_prompt: str, mode: str) -> str:
    """Enhance the user prompt based on generation mode."""
    if mode == "base_only":
        return (
            f"{user_prompt}\n\n"
            "IMPORTANT: Do NOT include any text, words, letters, numbers, watermarks, "
            "or logos in the image. The image should be a clean visual scene only, "
            "suitable for adding text overlays later."
        )
    else:
        # complete mode — prompt should already include text instructions
        return user_prompt


def generate_image(
    prompt: str,
    width: int = 1200,
    height: int = 675,
    mode: str = "base_only",
    model: str = DEFAULT_MODEL,
    output_path: Optional[str] = None,
    dry_run: bool = False,
    daily_cap_override: Optional[int] = None,
    per_run_cap_override: Optional[int] = None,
) -> Optional[str]:
    """
    Generate an image using the Gemini API.

    Args:
        prompt: Visual description for the image
        width: Target width in pixels
        height: Target height in pixels
        mode: "base_only" (no text) or "complete" (with text/branding)
        model: Gemini model ID
        output_path: Where to save the image. If None, auto-generates a path.
        dry_run: If True, skip the API call and show what would happen.
        daily_cap_override: Override the daily image cap for this call.
        per_run_cap_override: Override the per-run image cap for this call.

    Returns:
        Path to the saved image, or None if generation failed.
    """
    global _run_image_count

    aspect_ratio = get_aspect_ratio(width, height)
    image_size = get_image_size(model, max(width, height))
    cost_est = COST_PER_IMAGE.get(model, 0.10)

    # ── Guardrail check ──
    if not check_guardrails(model, daily_cap_override, per_run_cap_override):
        return None

    # ── Dry run mode ──
    if dry_run:
        print(f"\n  DRY RUN — No API call made")
        print(f"  Would generate: {width}x{height} ({aspect_ratio})")
        print(f"  Model: {model}")
        print(f"  Mode: {mode}")
        print(f"  Estimated cost: ~${cost_est:.2f}")
        print(f"  Output: {output_path or 'auto-generated'}")
        print(f"  Prompt preview: {prompt[:120]}...")
        return "DRY_RUN"

    client = get_client()
    full_prompt = build_prompt(prompt, mode)

    # Build image config
    image_config_kwargs = {"aspect_ratio": aspect_ratio}
    if image_size:
        image_config_kwargs["image_size"] = image_size

    config = types.GenerateContentConfig(
        response_modalities=["IMAGE"],
        image_config=types.ImageConfig(**image_config_kwargs),
    )

    # Retry loop for rate limits
    for attempt in range(1, MAX_RETRIES + 1):
        try:
            print(f"  Generating image (attempt {attempt}/{MAX_RETRIES})...")
            print(f"  Model: {model}")
            print(f"  Aspect ratio: {aspect_ratio}")
            if image_size:
                print(f"  Resolution: {image_size}")
            print(f"  Mode: {mode}")

            response = client.models.generate_content(
                model=model,
                contents=[full_prompt],
                config=config,
            )

            # Extract image from response
            for part in response.parts:
                if part.inline_data is not None:
                    # Convert raw image bytes to PIL Image
                    image_bytes = part.inline_data.data
                    pil_image = Image.open(io.BytesIO(image_bytes))
                    print(f"  Generated image: {pil_image.size[0]}x{pil_image.size[1]}")

                    # Resize to exact target dimensions
                    if pil_image.size != (width, height):
                        print(f"  Resizing to {width}x{height}")
                        pil_image = pil_image.resize((width, height), Image.LANCZOS)

                    # Determine output path
                    if output_path is None:
                        output_path = f"gemini_output_{width}x{height}.png"

                    # Ensure output directory exists
                    out_dir = Path(output_path).parent
                    out_dir.mkdir(parents=True, exist_ok=True)

                    # Save
                    pil_image.save(output_path, "PNG", optimize=True)
                    print(f"  Saved: {output_path}")

                    # Log success and increment counters
                    _run_image_count += 1
                    _log_generation(model, mode, f"{width}x{height}",
                                    success=True, output_path=output_path)
                    return str(output_path)

            print("  Warning: Response contained no image data.")
            _log_generation(model, mode, f"{width}x{height}", success=False)
            if attempt < MAX_RETRIES:
                print(f"  Retrying in {RETRY_DELAY_SECONDS}s...")
                time.sleep(RETRY_DELAY_SECONDS)

        except Exception as e:
            error_msg = str(e)
            if "429" in error_msg or "RESOURCE_EXHAUSTED" in error_msg:
                wait = RETRY_DELAY_SECONDS * attempt
                print(f"  Rate limited. Waiting {wait}s before retry...")
                time.sleep(wait)
            else:
                print(f"  Error: {error_msg}")
                _log_generation(model, mode, f"{width}x{height}", success=False)
                if attempt < MAX_RETRIES:
                    print(f"  Retrying in {RETRY_DELAY_SECONDS}s...")
                    time.sleep(RETRY_DELAY_SECONDS)
                else:
                    print("  All retries exhausted.")
                    return None

    return None


def generate_story_images(
    prompt: str,
    story_number: int,
    content_folder: str,
    mode: str = "base_only",
    model: str = DEFAULT_MODEL,
    dry_run: bool = False,
    daily_cap_override: Optional[int] = None,
    per_run_cap_override: Optional[int] = None,
    platform: str = "social",
) -> dict:
    """
    Generate images for a single story.

    By default, generates a single 4:5 vertical (1080x1350) image used for ALL
    social media posts. Use platform="article" to generate a 1.91:1 landscape
    article hero image instead.

    Args:
        prompt: Visual description from image concepts
        story_number: Story number (1-8)
        content_folder: Path to the dated content folder
        mode: "base_only" or "complete"
        model: Gemini model ID
        dry_run: If True, skip API calls
        daily_cap_override: Override daily cap
        per_run_cap_override: Override per-run cap
        platform: "social" (4:5 vertical, default) or "article" (1.91:1 landscape)

    Returns:
        Dict with image paths (or None for failures)
    """
    gen_dir = Path(content_folder) / "generated-images"
    gen_dir.mkdir(parents=True, exist_ok=True)

    results = {}

    if platform == "article":
        # Article hero image (1200x630, 1.91:1 landscape)
        print(f"\n--- Story {story_number}: Article Hero Image (1200x630) ---")
        path = generate_image(
            prompt=prompt,
            width=1200,
            height=630,
            mode=mode,
            model=model,
            output_path=str(gen_dir / f"story-{story_number}-article.png"),
            dry_run=dry_run,
            daily_cap_override=daily_cap_override,
            per_run_cap_override=per_run_cap_override,
        )
        results["article_image_path"] = path
    else:
        # Social media image (1080x1350, 4:5 vertical — all platforms)
        print(f"\n--- Story {story_number}: Social Image (1080x1350, 4:5) ---")
        social_path = generate_image(
            prompt=prompt,
            width=1080,
            height=1350,
            mode=mode,
            model=model,
            output_path=str(gen_dir / f"story-{story_number}-social.png"),
            dry_run=dry_run,
            daily_cap_override=daily_cap_override,
            per_run_cap_override=per_run_cap_override,
        )
        results["social_image_path"] = social_path

    return results


# ── CLI Interface ────────────────────────────────────────────

def parse_dimensions(dim_str: str) -> Tuple[int, int]:
    """Parse a 'WIDTHxHEIGHT' string."""
    parts = dim_str.lower().split("x")
    if len(parts) != 2:
        raise ValueError(f"Invalid dimensions format: {dim_str}. Use WIDTHxHEIGHT (e.g., 1200x675)")
    return int(parts[0]), int(parts[1])


def main():
    parser = argparse.ArgumentParser(
        description="Generate images using the Gemini API for FanGear HQ content pipeline"
    )
    parser.add_argument(
        "--prompt", required=False, default=None,
        help="Visual description for the image"
    )
    parser.add_argument(
        "--dimensions", default="1200x675",
        help="Target dimensions as WIDTHxHEIGHT (default: 1200x675)"
    )
    parser.add_argument(
        "--mode", choices=["base_only", "complete"], default="base_only",
        help="Generation mode: base_only (no text) or complete (with text)"
    )
    parser.add_argument(
        "--model", default=DEFAULT_MODEL,
        help=f"Gemini model ID (default: {DEFAULT_MODEL})"
    )
    parser.add_argument(
        "--output", default=None,
        help="Output file path (default: auto-generated)"
    )
    parser.add_argument(
        "--story-number", type=int, default=None,
        help="Generate both X and Facebook images for a story number"
    )
    parser.add_argument(
        "--content-folder", default=None,
        help="Content folder path (used with --story-number)"
    )

    # Guardrail flags
    parser.add_argument(
        "--budget", action="store_true",
        help="Show usage and spending report, then exit"
    )
    parser.add_argument(
        "--dry-run", action="store_true",
        help="Preview what would be generated without calling the API"
    )
    parser.add_argument(
        "--daily-cap", type=int, default=None,
        help=f"Override daily image cap (default: {DAILY_CAP_DEFAULT})"
    )
    parser.add_argument(
        "--per-run-cap", type=int, default=None,
        help=f"Override per-run image cap (default: {PER_RUN_CAP_DEFAULT})"
    )

    args = parser.parse_args()

    # Budget report mode
    if args.budget:
        print_budget_report()
        return

    # Require prompt for generation
    if not args.prompt:
        print("Error: --prompt is required (unless using --budget)")
        parser.print_help()
        sys.exit(1)

    # Story mode: generate both platform images
    if args.story_number is not None:
        if not args.content_folder:
            print("Error: --content-folder is required when using --story-number")
            sys.exit(1)

        results = generate_story_images(
            prompt=args.prompt,
            story_number=args.story_number,
            content_folder=args.content_folder,
            mode=args.mode,
            model=args.model,
            dry_run=args.dry_run,
            daily_cap_override=args.daily_cap,
            per_run_cap_override=args.per_run_cap,
        )
        print(f"\nResults:")
        print(f"  X image:        {results.get('x_image_path', 'FAILED')}")
        print(f"  Facebook image: {results.get('facebook_image_path', 'FAILED')}")
        return

    # Single image mode
    width, height = parse_dimensions(args.dimensions)
    result = generate_image(
        prompt=args.prompt,
        width=width,
        height=height,
        mode=args.mode,
        model=args.model,
        output_path=args.output,
        dry_run=args.dry_run,
        daily_cap_override=args.daily_cap,
        per_run_cap_override=args.per_run_cap,
    )

    if result:
        print(f"\nSuccess: {result}")
    else:
        print("\nFailed to generate image.")
        sys.exit(1)


if __name__ == "__main__":
    main()
