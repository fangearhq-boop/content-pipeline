#!/usr/bin/env python3
"""
FanGear HQ — Social Image Compositor
Composites final social media images from Gemini base images + text overlays.

Layout: Image fills ~2/3 of frame, text overlay bar fills ~1/3.
- Headline: Poppins Bold, white, as large as possible
- Subtitle: Nunito SemiBold (or variable), accent color
- No website URLs, no body text, no dead space.

Usage:
    python composite-social-image.py <base_image> <output_path> \
        --headline "Headline Text" --subtitle "Subtitle Text" \
        --platform x|facebook \
        [--subtitle-color "#F4C542"] \
        [--bar-color "#2C3E50"] [--bar-opacity 0.85] \
        [--bar-position bottom|top]

    Or import and use composite_image() directly.
"""

import os
import sys
import argparse
import textwrap
from PIL import Image, ImageDraw, ImageFont

# --- Paths ---
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ENGINE_DIR = os.path.dirname(SCRIPT_DIR)
FONTS_DIR = os.path.join(ENGINE_DIR, "fonts")

FONT_HEADLINE = os.path.join(FONTS_DIR, "Poppins-Bold.ttf")
FONT_SUBTITLE = os.path.join(FONTS_DIR, "Nunito-Variable.ttf")

# Fallbacks if brand fonts not found
FONT_FALLBACK = "arial.ttf"

# --- Platform dimensions ---
PLATFORMS = {
    # Social media posts — all use 4:5 vertical for maximum mobile feed presence
    "x": (1080, 1350),        # 4:5 vertical (optimal for mobile feed)
    "facebook": (1080, 1350), # 4:5 vertical (optimal for mobile feed)
    "social": (1080, 1350),   # Generic alias — same 4:5 for any social platform
    # Article hero images — wide landscape for embedding in articles
    "article": (1200, 630),   # 1.91:1 landscape (article hero / Open Graph)
}

# --- Default brand colors ---
DEFAULT_BAR_COLOR = "#2C3E50"
DEFAULT_BAR_OPACITY = 0.85
DEFAULT_HEADLINE_COLOR = "#FFFFFF"
DEFAULT_SUBTITLE_COLOR = "#F4C542"  # Soft Gold
SUBTITLE_URGENT_COLOR = "#FF6F61"   # Warm Coral


def hex_to_rgb(hex_color):
    """Convert hex color string to RGB tuple."""
    hex_color = hex_color.lstrip("#")
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))


def load_font(font_path, size):
    """Load a font, falling back to system font if needed."""
    try:
        return ImageFont.truetype(font_path, size)
    except (OSError, IOError):
        try:
            return ImageFont.truetype(FONT_FALLBACK, size)
        except (OSError, IOError):
            return ImageFont.load_default()


def fit_text_to_area(draw, text, font_path, max_width, max_height, max_size,
                     min_size=20, step=2, max_lines=3, line_spacing=1.12):
    """
    Find the LARGEST font size where text fits within max_width x max_height.
    Prefers wrapping to 2-3 lines at a big font over shrinking to one tiny line.
    Returns (font, wrapped_lines, font_size).

    Strategy: For each font size (largest first), try 1-line, 2-line, 3-line
    wraps. Accept the first combo where all lines fit width AND total height
    fits the budget. This means a 2-line headline at 120px beats a 1-line at 60px.
    """
    words = text.split()

    for size in range(max_size, min_size - 1, -step):
        font = load_font(font_path, size)

        # Measure single character height for this font size
        sample_bbox = draw.textbbox((0, 0), "Ag", font=font)
        char_h = sample_bbox[3] - sample_bbox[1]

        # Try wrapping at different points (fewest lines first)
        for num_lines in range(1, max_lines + 1):
            # Check if this many lines even fits vertically
            total_h = int(char_h * num_lines + char_h * (line_spacing - 1) * (num_lines - 1))
            if total_h > max_height:
                continue  # Too tall, try more lines won't help — next font size

            if num_lines == 1:
                # Try single line
                bbox = draw.textbbox((0, 0), text, font=font)
                if (bbox[2] - bbox[0]) <= max_width:
                    return font, [text], size
            else:
                # Try wrapping — find a wrap width that produces exactly num_lines
                # and where every line fits max_width
                for max_chars in range(len(text) - 1, 4, -1):
                    lines = textwrap.wrap(text, width=max_chars)
                    if len(lines) != num_lines:
                        continue
                    # Check all lines fit width
                    all_fit = True
                    for line in lines:
                        bbox = draw.textbbox((0, 0), line, font=font)
                        if (bbox[2] - bbox[0]) > max_width:
                            all_fit = False
                            break
                    if all_fit:
                        return font, lines, size

        # If even max_lines doesn't work at this size, try next smaller size

    # Absolute fallback
    font = load_font(font_path, min_size)
    lines = textwrap.wrap(text, width=15)
    return font, lines, min_size


def get_text_block_height(draw, lines, font, line_spacing=1.15):
    """Calculate total height of a multi-line text block."""
    total = 0
    for i, line in enumerate(lines):
        bbox = draw.textbbox((0, 0), line, font=font)
        line_h = bbox[3] - bbox[1]
        total += line_h
        if i < len(lines) - 1:
            total += int(line_h * (line_spacing - 1))
    return total


def composite_image(
    base_image_path,
    output_path,
    headline,
    subtitle,
    platform="x",
    subtitle_color=DEFAULT_SUBTITLE_COLOR,
    bar_color=DEFAULT_BAR_COLOR,
    bar_opacity=DEFAULT_BAR_OPACITY,
    bar_position="bottom",
    headline_color=DEFAULT_HEADLINE_COLOR,
):
    """
    Composite a final social media image.

    Args:
        base_image_path: Path to the Gemini-generated base image
        output_path: Where to save the final composite
        headline: Main headline text (large, bold)
        subtitle: Subtitle text (smaller, accent color)
        platform: "x" or "facebook"
        subtitle_color: Hex color for subtitle text
        bar_color: Hex color for overlay bar background
        bar_opacity: Opacity of overlay bar (0.0-1.0)
        bar_position: "bottom" or "top"
        headline_color: Hex color for headline text

    Returns:
        output_path on success
    """
    # Target dimensions
    target_w, target_h = PLATFORMS.get(platform, PLATFORMS["x"])

    # Bar height = 1/3 of total image
    bar_h = int(target_h / 3)
    padding_x = int(target_w * 0.025)  # 2.5% horizontal padding — tight
    padding_y = int(bar_h * 0.03)      # 3% vertical padding — minimal
    text_area_w = target_w - (2 * padding_x)

    # Load base image and crop-to-fill (no stretching/distortion)
    base = Image.open(base_image_path).convert("RGBA")
    src_w, src_h = base.size
    target_ratio = target_w / target_h
    src_ratio = src_w / src_h

    if src_ratio > target_ratio:
        # Source is wider — crop sides, keep full height
        new_w = int(src_h * target_ratio)
        left = (src_w - new_w) // 2
        base = base.crop((left, 0, left + new_w, src_h))
    elif src_ratio < target_ratio:
        # Source is taller — crop top/bottom, keep full width
        new_h = int(src_w / target_ratio)
        top = (src_h - new_h) // 2
        base = base.crop((0, top, src_w, top + new_h))

    base = base.resize((target_w, target_h), Image.LANCZOS)

    # Create overlay bar
    bar_rgb = hex_to_rgb(bar_color)
    bar_alpha = int(bar_opacity * 255)
    overlay = Image.new("RGBA", (target_w, bar_h), (*bar_rgb, bar_alpha))

    # Draw text on the overlay bar
    draw_overlay = ImageDraw.Draw(overlay)

    # Calculate space budget inside bar — text should FILL the bar
    usable_h = bar_h - (2 * padding_y)
    headline_budget = int(usable_h * 0.68)  # 68% for headline
    subtitle_budget = int(usable_h * 0.28)  # 28% for subtitle
    gap = int(usable_h * 0.04)              # 4% gap — tight

    # Fit headline — largest font that fits, wrapping to 2-3 lines if needed
    max_headline_size = int(headline_budget * 0.95)
    h_font, h_lines, h_size = fit_text_to_area(
        draw_overlay, headline, FONT_HEADLINE,
        text_area_w, headline_budget, max_headline_size,
        min_size=36, step=2, max_lines=3
    )

    # Fit subtitle — wrapping to 2 lines if needed
    max_subtitle_size = int(subtitle_budget * 0.90)
    s_font, s_lines, s_size = fit_text_to_area(
        draw_overlay, subtitle, FONT_SUBTITLE,
        text_area_w, subtitle_budget, max_subtitle_size,
        min_size=20, step=2, max_lines=2
    )

    # Calculate actual text heights
    h_block_h = get_text_block_height(draw_overlay, h_lines, h_font)
    s_block_h = get_text_block_height(draw_overlay, s_lines, s_font)
    total_text_h = h_block_h + gap + s_block_h

    # Vertically center the text block within the bar
    start_y = max(padding_y, (bar_h - total_text_h) // 2)

    # Draw headline lines
    h_color = hex_to_rgb(headline_color)
    y = start_y
    for line in h_lines:
        bbox = draw_overlay.textbbox((0, 0), line, font=h_font)
        line_w = bbox[2] - bbox[0]
        line_h = bbox[3] - bbox[1]
        x = (target_w - line_w) // 2  # Center horizontally
        draw_overlay.text((x, y), line, font=h_font, fill=(*h_color, 255))
        y += int(line_h * 1.1)

    # Draw subtitle lines
    y += gap
    s_color_rgb = hex_to_rgb(subtitle_color)
    for line in s_lines:
        bbox = draw_overlay.textbbox((0, 0), line, font=s_font)
        line_w = bbox[2] - bbox[0]
        line_h = bbox[3] - bbox[1]
        x = (target_w - line_w) // 2  # Center horizontally
        draw_overlay.text((x, y), line, font=s_font, fill=(*s_color_rgb, 255))
        y += int(line_h * 1.1)

    # Composite: paste overlay bar onto base image
    if bar_position == "bottom":
        bar_y = target_h - bar_h
    else:
        bar_y = 0

    base.paste(overlay, (0, bar_y), overlay)

    # Convert to RGB for PNG/JPEG output
    final = base.convert("RGB")
    final.save(output_path, quality=95)

    return output_path


def main():
    parser = argparse.ArgumentParser(description="Composite social media image")
    parser.add_argument("base_image", help="Path to base Gemini image")
    parser.add_argument("output", help="Output path for final image")
    parser.add_argument("--headline", required=True, help="Headline text")
    parser.add_argument("--subtitle", required=True, help="Subtitle text")
    parser.add_argument("--platform", default="x", choices=["x", "facebook"])
    parser.add_argument("--subtitle-color", default=DEFAULT_SUBTITLE_COLOR)
    parser.add_argument("--bar-color", default=DEFAULT_BAR_COLOR)
    parser.add_argument("--bar-opacity", type=float, default=DEFAULT_BAR_OPACITY)
    parser.add_argument("--bar-position", default="bottom", choices=["bottom", "top"])
    parser.add_argument("--headline-color", default=DEFAULT_HEADLINE_COLOR)

    args = parser.parse_args()

    result = composite_image(
        base_image_path=args.base_image,
        output_path=args.output,
        headline=args.headline,
        subtitle=args.subtitle,
        platform=args.platform,
        subtitle_color=args.subtitle_color,
        bar_color=args.bar_color,
        bar_opacity=args.bar_opacity,
        bar_position=args.bar_position,
        headline_color=args.headline_color,
    )
    print(f"Created: {result}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
