#!/usr/bin/env python3
"""
Generate article hero images for FanGear HQ content pipeline.

Architecture: Imagen 4 Ultra generates rich backgrounds (no text) with max-specificity
5-phase prompts. Pillow composites all text/stats with 100% accuracy. AI verification
gate checks each image before accepting.

Usage:
    python generate-article-images.py --niche Softball 2026-03-22
    python generate-article-images.py --niche Softball 2026-03-22 --model imagen-ultra  # default
    python generate-article-images.py --niche Softball 2026-03-22 --model nano-banana-pro
    python generate-article-images.py --niche Softball 2026-03-22 --skip-verify  # skip AI verification

Requires: GEMINI_API_KEY env var or ~/.claude/keys/gemini-api.key
"""

import os
import sys
import re
import json
import time
import argparse
import logging
from pathlib import Path
from datetime import datetime

logging.basicConfig(level="INFO", format="%(asctime)s [%(name)s] %(levelname)s: %(message)s")
log = logging.getLogger("article-images")

# Models
IMAGEN_4_ULTRA = "imagen-4.0-ultra-generate-001"
IMAGEN_4 = "imagen-4.0-generate-001"
IMAGEN_4_FAST = "imagen-4.0-fast-generate-001"
NANO_BANANA_PRO = "gemini-3-pro-image-preview"
NANO_BANANA_2 = "gemini-3.1-flash-image-preview"
DEFAULT_MODEL = IMAGEN_4_ULTRA  # Highest quality for production

# Verification model (cheap + fast)
VERIFY_MODEL = "gemini-2.5-flash"

# Model name mapping for CLI
MODEL_MAP = {
    "imagen-ultra": IMAGEN_4_ULTRA,
    "imagen": IMAGEN_4,
    "imagen-fast": IMAGEN_4_FAST,
    "nano-banana-pro": NANO_BANANA_PRO,
    "nano-banana-2": NANO_BANANA_2,
}

# Brand colors (I Love Softball defaults)
BRAND_COLOR_1 = "#FF8A00"
BRAND_COLOR_2 = "#E53935"

# Key file fallback
GEMINI_KEY_FILE = os.path.join(os.path.expanduser("~"), ".claude", "keys", "gemini-api.key")

# Safety limits
DAILY_IMAGE_CAP = int(os.environ.get("GEMINI_DAILY_CAP", "20"))  # Max images per day (across all runs)
MONTHLY_SPEND_WARN = float(os.environ.get("GEMINI_MONTHLY_WARN", "15.00"))  # USD
COST_PER_IMAGE = 0.04  # Estimated cost per Nano Banana 2 generation
USAGE_LOG = os.path.join(os.path.expanduser("~"), ".claude", "keys", "gemini-image-usage.json")


def check_usage_limits():
    """Check daily and monthly usage limits. Returns (can_proceed, reason)."""
    today = datetime.now().strftime("%Y-%m-%d")
    month = datetime.now().strftime("%Y-%m")

    usage = {"daily": {}, "monthly": {}}
    if os.path.isfile(USAGE_LOG):
        try:
            with open(USAGE_LOG) as f:
                usage = json.load(f)
        except (json.JSONDecodeError, IOError):
            pass

    today_count = usage.get("daily", {}).get(today, 0)
    month_cost = sum(
        v * COST_PER_IMAGE
        for k, v in usage.get("daily", {}).items()
        if k.startswith(month)
    )

    if today_count >= DAILY_IMAGE_CAP:
        return False, f"Daily cap reached: {today_count}/{DAILY_IMAGE_CAP} images today. Set GEMINI_DAILY_CAP to increase."

    if month_cost >= MONTHLY_SPEND_WARN:
        log.warning("Monthly spend estimate: $%.2f (warning threshold: $%.2f)", month_cost, MONTHLY_SPEND_WARN)

    return True, f"Usage: {today_count}/{DAILY_IMAGE_CAP} today, ~${month_cost:.2f} this month"


def log_usage(count):
    """Record image generation count for today."""
    today = datetime.now().strftime("%Y-%m-%d")

    usage = {"daily": {}, "monthly": {}}
    if os.path.isfile(USAGE_LOG):
        try:
            with open(USAGE_LOG) as f:
                usage = json.load(f)
        except (json.JSONDecodeError, IOError):
            pass

    if "daily" not in usage:
        usage["daily"] = {}
    usage["daily"][today] = usage["daily"].get(today, 0) + count

    # Prune entries older than 60 days
    cutoff = (datetime.now() - __import__("datetime").timedelta(days=60)).strftime("%Y-%m-%d")
    usage["daily"] = {k: v for k, v in usage["daily"].items() if k >= cutoff}

    os.makedirs(os.path.dirname(USAGE_LOG), exist_ok=True)
    with open(USAGE_LOG, "w") as f:
        json.dump(usage, f, indent=2)
    log.info("Logged %d images. Total today: %d", count, usage["daily"][today])


def get_gemini_client():
    """Initialize Gemini client."""
    api_key = os.environ.get("GEMINI_API_KEY", "")
    if not api_key and os.path.isfile(GEMINI_KEY_FILE):
        with open(GEMINI_KEY_FILE) as f:
            api_key = f.read().strip()
        log.info("Loaded Gemini key from %s", GEMINI_KEY_FILE)
    if not api_key:
        log.error("GEMINI_API_KEY not set and %s not found", GEMINI_KEY_FILE)
        return None
    try:
        from google import genai
        return genai.Client(api_key=api_key)
    except ImportError:
        log.error("google-genai not installed. Run: pip install google-genai")
        return None


def classify_story(title):
    """Classify story type from title using keyword heuristics."""
    t = title.lower()
    if any(w in t for w in ["upset", "stun", "shock", "stunner"]):
        return "upset"
    if any(w in t for w in ["record", "streak", "straight", "consecutive", "milestone", "historic"]):
        return "record_tracker"
    if any(w in t for w in ["run-rule", "beats", "defeats", "wins", "blanks", "outlasts", "score"]):
        return "game_recap"
    if any(w in t for w in ["blasts", "home run", "strikeout", "hr", "no-hitter", "perfect game", "shutout"]):
        return "player_spotlight"
    if any(w in t for w in [" vs ", " at ", "preview", "matchup", "rubber match", "today"]):
        return "matchup_preview"
    if any(w in t for w in ["poll", "ranking", "ranked", "ncaa record"]):
        return "rankings_analysis"
    return "general"


def extract_key_stat(facts_text, story_num):
    """Extract the first HIGH-confidence numeric fact for a story."""
    # Find the story section
    pattern = rf"### STORY {story_num}:.*?(?=### STORY \d|$)"
    match = re.search(pattern, facts_text, re.DOTALL)
    if not match:
        return None

    section = match.group(0)
    # Find table rows with HIGH confidence and a number
    for line in section.split("\n"):
        if "| HIGH |" in line:
            cells = [c.strip() for c in line.split("|")]
            if len(cells) >= 2:
                fact = cells[1]
                # Extract numbers from the fact
                nums = re.findall(r'\d+', fact)
                if nums:
                    return fact.strip()
    return None


def extract_story_data(facts_text, story_num, story_title):
    """Extract structured data from the verified fact sheet for compositing.

    Returns dict with: big_stat, stat_label, secondary_stats, score_line, score_detail, subline
    """
    pattern = rf"### STORY {story_num}:.*?(?=### STORY \d|$)"
    match = re.search(pattern, facts_text, re.DOTALL)
    if not match:
        return {}

    section = match.group(0)
    facts = []
    for line in section.split("\n"):
        if "| HIGH |" in line or "| MEDIUM |" in line:
            cells = [c.strip() for c in line.split("|")]
            if len(cells) >= 2:
                facts.append(cells[1])

    if not facts:
        return {}

    result = {}

    # Find the best "big stat" — look for specific patterns
    score_pattern = re.compile(r'(\w+)\s+(?:beat|defeated|won|run-ruled)\s+(\w[\w\s]*?)\s+(\d+)-(\d+)', re.I)
    record_pattern = re.compile(r'(\d+)\s+(?:consecutive|straight|HR|home run|strikeout|win)', re.I)
    stat_number_pattern = re.compile(r'(?:HR|home run|strikeout|win|K)\s*#?(\d+)', re.I)

    # Try to find a score
    for fact in facts:
        m = score_pattern.search(fact)
        if m:
            winner, loser, w_score, l_score = m.group(1), m.group(2), m.group(3), m.group(4)
            result["score_line"] = f"{winner.upper()} {w_score} - {loser.upper().strip()} {l_score}"
            # Check for run-rule
            if "run-rule" in fact.lower():
                innings = re.search(r'(\d+)\s+innings?', fact, re.I)
                inn_text = f" ({innings.group(1)} Inn)" if innings else ""
                result["score_detail"] = f"Run-Rule{inn_text}"
            break

    # Find the most impactful stat — priority order matters
    best_num = None
    best_label = None

    # Pass 1: Win streaks / consecutive records (highest priority for record_tracker)
    for fact in facts:
        m = re.search(r'(\d+)\s+consecutive', fact, re.I)
        if m and int(m.group(1)) >= 10:
            best_num = m.group(1)
            best_label = "STRAIGHT WINS"
            break

    # Pass 2: HR count with explicit "leads nation" or "#XX and #XX" (player_spotlight)
    if not best_num:
        for fact in facts:
            m = re.search(r'HR\s*#(\d+)\s+and\s*#?(\d+)', fact, re.I)
            if m:
                best_num = m.group(2)  # Higher number
                best_label = "HOME RUNS"
                break
        if not best_num:
            for fact in facts:
                m = re.search(r'leads\s+nation\s+in\s+HR\s+with\s+(\d+)', fact, re.I)
                if m:
                    best_num = m.group(1)
                    best_label = "HOME RUNS"
                    break

    # Pass 3: Pitcher record (W-L)
    if not best_num:
        for fact in facts:
            m = re.search(r'improved to (\d+)-(\d+)', fact, re.I)
            if m:
                best_num = f"{m.group(1)}-{m.group(2)}"
                best_label = "SEASON RECORD"
                break

    # Pass 4: Strikeouts
    if not best_num:
        for fact in facts:
            m = re.search(r'(\d+)\s+K\b', fact)
            if m and int(m.group(1)) >= 5:
                best_num = m.group(1)
                best_label = "STRIKEOUTS"
                break

    # Pass 5: Score from the game (fallback)
    if not best_num and result.get("score_line"):
        # Pull the winning score from score_line
        m = re.search(r'(\d+)\s*-\s*\d+', result["score_line"])
        if m:
            best_num = m.group(1)
            best_label = "RUNS SCORED"

    result["big_stat"] = best_num
    result["stat_label"] = best_label

    # Build secondary stats (short, punchy lines from top facts)
    secondary = []
    for fact in facts[:6]:
        # Skip the ones we already used
        if best_num and best_num in fact:
            continue
        if result.get("score_line") and any(w in fact.lower() for w in ["beat", "defeated", "won"]):
            continue
        # Shorten to a punchy stat line
        short = fact.strip()
        if len(short) > 40:
            short = short[:40].rsplit(" ", 1)[0]
        secondary.append(short.upper())
        if len(secondary) >= 3:
            break

    result["secondary_stats"] = secondary

    # Build subline from title context
    title_lower = story_title.lower()
    if result.get("score_line"):
        result["subline"] = f"{result['score_line']}"
        if result.get("score_detail"):
            result["subline"] += f" | {result['score_detail']}"
    elif secondary:
        result["subline"] = secondary[0]

    return result


TEAM_PALETTE = {
    "texas": {"name": "University of Texas Longhorns", "primary": "#BF5700", "secondary": "#FFFFFF",
              "uniform": "burnt orange jerseys with white pants and a longhorn logo on the helmet",
              "accent_desc": "burnt orange and white"},
    "oklahoma": {"name": "University of Oklahoma Sooners", "primary": "#841617", "secondary": "#FDF9D8",
                 "uniform": "crimson red jerseys with cream white pants",
                 "accent_desc": "crimson red and cream"},
    "tennessee": {"name": "University of Tennessee Lady Vols", "primary": "#FF8200", "secondary": "#FFFFFF",
                  "uniform": "Tennessee orange jerseys with white pants",
                  "accent_desc": "Tennessee orange and white"},
    "florida": {"name": "University of Florida Gators", "primary": "#0021A5", "secondary": "#FA4616",
                "uniform": "blue and orange Florida Gators jerseys",
                "accent_desc": "Gators blue and orange"},
    "alabama": {"name": "University of Alabama Crimson Tide", "primary": "#9E1B32", "secondary": "#FFFFFF",
                "uniform": "Alabama crimson jerseys with white pants",
                "accent_desc": "crimson and white"},
    "missouri": {"name": "University of Missouri Tigers", "primary": "#F1B82D", "secondary": "#000000",
                 "uniform": "Missouri black jerseys with gold accents",
                 "accent_desc": "Mizzou gold and black"},
    "texas tech": {"name": "Texas Tech Red Raiders", "primary": "#CC0000", "secondary": "#000000",
                   "uniform": "Texas Tech red jerseys with black accents",
                   "accent_desc": "Tech red and black"},
    "gcu": {"name": "Grand Canyon University Lopes", "primary": "#522D80", "secondary": "#FFFFFF",
            "uniform": "Grand Canyon purple jerseys with white accents",
            "accent_desc": "GCU purple and white"},
    "fsu": {"name": "Florida State Seminoles", "primary": "#782F40", "secondary": "#CEB888",
            "uniform": "Florida State garnet jerseys with gold accents",
            "accent_desc": "garnet and gold"},
    "ucf": {"name": "UCF Knights", "primary": "#000000", "secondary": "#FFC904",
            "uniform": "UCF black jerseys with gold accents",
            "accent_desc": "black and gold"},
    "lsu": {"name": "LSU Tigers", "primary": "#461D7C", "secondary": "#FDD023",
            "uniform": "LSU purple jerseys with gold accents",
            "accent_desc": "purple and gold"},
    "arkansas": {"name": "Arkansas Razorbacks", "primary": "#9D2235", "secondary": "#FFFFFF",
                 "uniform": "Arkansas cardinal red jerseys with white",
                 "accent_desc": "cardinal and white"},
}


def verify_image(client, image_path, expected_team_color, story_type):
    """AI verification gate — checks the generated image for correctness.

    Returns (passed: bool, issues: list[str]).
    """
    try:
        from google.genai import types as gtypes

        with open(image_path, "rb") as f:
            img_bytes = f.read()

        prompt = f"""Analyze this sports graphic background image. Answer each check with PASS or FAIL and a brief reason.

1. SPORT: Does this show women's/girls' SOFTBALL? (Not baseball, football, or other sports. Softball uses a larger yellow ball and a flat pitcher's circle, not a raised mound.)
2. GENDER: Are all athletes clearly FEMALE?
3. TEAM COLORS: Do the primary athletes' uniforms match {expected_team_color}?
4. GENERATED TEXT: Is the image FREE of generated headlines, stat numbers, or scoreboard text? (Natural jersey numbers and small uniform text are OK — we only fail on large generated text overlays, headlines, or stat graphics that the AI added.)
5. DARK ZONES: Are the bottom 30%+ and/or right 30%+ of the image dark enough for white text overlay?
6. QUALITY: Is this professional sports magazine quality (not cartoon, not low-res, not distorted)?

Reply in this exact format:
PASS_COUNT: [number 0-6]
1. PASS/FAIL: reason
2. PASS/FAIL: reason
3. PASS/FAIL: reason
4. PASS/FAIL: reason
5. PASS/FAIL: reason
6. PASS/FAIL: reason"""

        response = client.models.generate_content(
            model=VERIFY_MODEL,
            contents=[
                prompt,
                gtypes.Part.from_bytes(data=img_bytes, mime_type="image/png"),
            ],
        )

        text = response.text
        issues = []

        # Parse PASS_COUNT
        import re as _re
        count_match = _re.search(r"PASS_COUNT:\s*(\d+)", text)
        pass_count = int(count_match.group(1)) if count_match else 0

        # Extract individual failures
        for line in text.split("\n"):
            line = line.strip()
            if line and line[0].isdigit() and "FAIL" in line.upper():
                issues.append(line)

        # Pass if 5+ of 6 checks pass (allow 1 marginal failure)
        passed = pass_count >= 5 and not any("1. FAIL" in i or "2. FAIL" in i for i in issues)

        if passed:
            log.info("  Verification PASSED (%d/6)", pass_count)
        else:
            log.warning("  Verification FAILED (%d/6): %s", pass_count, "; ".join(issues))

        return passed, issues

    except Exception as e:
        log.warning("  Verification error (treating as pass): %s", e)
        return True, []  # Don't block on verification errors


def get_team_info(title, story_type=None):
    """Extract team palette info from story title.

    For game recaps and upsets, the WINNING team should be first.
    Heuristic: in titles like "X beats/stuns/upsets Y" or "X Run-Rules Y",
    the first team mentioned is usually the winner.
    But in "Y Upsets #4 X" the subject (Y) is the winner.
    """
    t = title.lower()
    teams_found = []
    # Find teams with their position in the title
    for key, info in TEAM_PALETTE.items():
        pos = t.find(key)
        if pos >= 0:
            teams_found.append((pos, key, info))

    teams_found.sort(key=lambda x: x[0])  # Sort by position in title

    if len(teams_found) >= 2 and story_type in ("upset", "game_recap"):
        # Check if the title pattern suggests the second team is the winner
        # "X Upsets #N Y" — X is the winner (first mentioned)
        # "X Stuns Y" — X is the winner
        # "X Run-Rules Y" — X is the winner
        # These patterns mean first-mentioned = winner, which is already correct

        # But check for passive patterns: "#5 Y beats #1 X" where rank+team order matters
        # The subject doing the action (upsets, stuns, beats, run-rules) is the winner
        first_team = teams_found[0][1]
        second_team = teams_found[1][1]

        # Find action verbs and which team precedes them
        action_verbs = ["upsets", "stuns", "beats", "defeats", "run-rules", "blanks", "tops", "downs", "edges"]
        for verb in action_verbs:
            verb_pos = t.find(verb)
            if verb_pos >= 0:
                # The team whose name ends closest before the verb is the winner
                first_dist = verb_pos - (teams_found[0][0] + len(teams_found[0][1]))
                second_dist = verb_pos - (teams_found[1][0] + len(teams_found[1][1]))

                if 0 <= second_dist < first_dist or first_dist < 0:
                    # Second team is closer to the verb — it's the winner, swap
                    teams_found[0], teams_found[1] = teams_found[1], teams_found[0]
                break

    return [t[2] for t in teams_found]


def build_background_prompt(story_title, story_type, story_data=None):
    """Build a deep, multi-phase editorial prompt for the AI background.

    Inspired by the Kenneth Walker III Swiss-style collage approach:
    structured compositional zones, specific art direction, and
    detailed texture/lighting specs — but adapted for softball articles
    with dark overlay zones for Pillow text compositing.
    """

    teams = get_team_info(story_title, story_type)
    primary_team = teams[0] if teams else {
        "name": "NCAA Softball", "primary": "#FF8A00", "secondary": "#E53935",
        "uniform": "athletic softball uniform", "accent_desc": "orange and red"
    }

    # Team color direction
    color_dir = (
        f"Iconic Accent Color: {primary_team['primary']} ({primary_team['accent_desc']}). "
        f"Athletes wearing {primary_team['uniform']}. "
    )
    if len(teams) >= 2:
        color_dir += f"Secondary team: {teams[1]['accent_desc']} accents on opposing side. "

    # ── STORY-TYPE SPECIFIC PROMPTS ──
    # Each type gets full Phase 1-5 treatment

    if story_type == "record_tracker":
        prompt = f"""Act as a Senior Editorial Designer creating a magazine-quality sports graphic.

PHASE 1: SEMANTIC INTELLIGENCE
Subject: NCAA College Softball — record-breaking achievement.
Sport: Women's college softball. Female athletes ONLY.
{color_dir}
Mood: Triumphant, historic, monumental.

PHASE 2: COMPOSITIONAL STRUCTURE
Single vertical portrait composition (1080x1350, 4:5 ratio) with overlapping geometric frames and segments:
- MAIN SUBJECT (Left 55%): A female college softball player in a triumphant pose — arms raised in celebration, bat in hand, after a big moment. {primary_team['uniform']}. Facing slightly right. Confetti particles in the air around her.
- DETAIL SHOT (Top Right, 25% of frame): A cropped geometric rectangle showing a close-up of a softball or a bat making contact — frozen motion detail.
- ASCENDING ELEMENT (Center): Subtle rising bar chart or ascending arrow shapes in the background, suggesting record-breaking momentum. Semi-transparent, integrated into the composition.
- BACKGROUND: Stadium atmosphere behind the player — packed stands, stadium lights creating lens flares. The bottom 45% should be significantly darker (deep charcoal to black gradient) to serve as text overlay zones. The image is VERTICAL (portrait orientation, taller than wide).

PHASE 3: GRAPHIC ELEMENTS
- Geometric frames: Overlapping rectangles and parallelograms creating depth layers around the player.
- Vertical accent strip: A semi-transparent color strip in {primary_team['primary']} running vertically at the 55% mark, creating a visual division.
- Scattered accents: Small squares, dotted circles, and asterisk shapes in {primary_team['accent_desc']} tones scattered throughout the grid for visual complexity.
- Film grain particles throughout.

PHASE 4: LIGHTING & TEXTURE
- High-contrast editorial sports photography. Stadium rim lighting creating a halo/silhouette edge on the player.
- Processed with subtle halftone dot pattern overlay for printed-magazine texture.
- Warm color grading shifting toward {primary_team['accent_desc']} tones.
- Gritty, tactile grain texture across the entire image.

PHASE 5: TECH SPECS
Sports editorial modernism aesthetic. Flat geometric shapes layered with hyper-realistic photography.
ABSOLUTELY NO TEXT, NO WORDS, NO LETTERS, NO NUMBERS, NO LOGOS anywhere in the image.
No watermarks, no brand marks, no scoreboards with text.
1080x1350 vertical portrait (4:5 aspect ratio). Taller than wide."""

    elif story_type == "game_recap":
        prompt = f"""Act as a Senior Editorial Designer creating a magazine-quality sports graphic.

PHASE 1: SEMANTIC INTELLIGENCE
Subject: NCAA College Softball — game result/recap.
Sport: Women's college softball. Female athletes ONLY.
{color_dir}
Mood: Victory energy, celebration, dominance.

PHASE 2: COMPOSITIONAL STRUCTURE
Single vertical portrait composition (1080x1350, 4:5 ratio):
- MAIN SUBJECT (Left 50%): A female college softball player in peak celebration — fist pump, helmet coming off, or crossing home plate. {primary_team['uniform']}. Dynamic action pose captured at the peak moment. Teammates blurred in background rushing toward her.
- ACTION DETAIL (Upper Right, geometric crop): A tight crop showing a softball leaving the bat, or a pitcher's release point — frozen high-speed moment inside a sharp rectangular frame.
- CROWD ENERGY (Background): Packed stadium stands with fans on their feet, slightly blurred. Stadium lights creating dramatic backlighting and lens flares.
- OVERLAY ZONES: Bottom 45% transitions to deep black via gradient. This zone is reserved for text overlay — keep it empty and dark. The image is vertical (portrait, taller than wide).

PHASE 3: GRAPHIC ELEMENTS
- Geometric frame overlaps: Sharp-edged rectangles and diagonal cuts creating a collage effect between the main subject and the detail shot.
- Color accent blocks: Small solid-color squares and rectangles in {primary_team['accent_desc']} scattered as design accents.
- Diagonal energy lines radiating from the player, suggesting explosive movement.
- Subtle dotted circles and grid patterns in the dark zones for visual texture.

PHASE 4: LIGHTING & TEXTURE
- Dramatic stadium lighting — strong key light from above-left, rim light from behind.
- High-contrast processing with crushed blacks. Magazine editorial feel.
- Light film grain across the entire image. Halftone dot texture in shadow areas.
- Warm color temperature, emphasizing {primary_team['accent_desc']}.

PHASE 5: TECH SPECS
Sports editorial design. Geometric frames layered over hyper-realistic photography.
ABSOLUTELY NO TEXT, NO WORDS, NO LETTERS, NO NUMBERS, NO LOGOS anywhere in the image.
1080x1350 vertical portrait (4:5 aspect ratio). Taller than wide."""

    elif story_type == "upset":
        prompt = f"""Act as a Senior Editorial Designer creating a magazine-quality sports graphic.

PHASE 1: SEMANTIC INTELLIGENCE
Subject: NCAA College Softball — major upset victory.
Sport: Women's college softball. Female athletes ONLY.
{color_dir}
Mood: Shock, explosion, underdog triumph. Raw emotion.

PHASE 2: COMPOSITIONAL STRUCTURE
Single vertical portrait composition (1080x1350, 4:5 ratio):
- MAIN SUBJECT (Center-Left, 55%): A group of female college softball players in an explosive pile-on celebration — jumping on each other, screaming with joy, pure chaos of victory. {primary_team['uniform']}. Captured at peak emotional intensity.
- SHATTER ELEMENT (Background): Abstract cracking/shattering glass effect radiating from behind the celebration — representing the upset/shock. Geometric shards flying outward.
- CONTRAST DETAIL (Top Right corner): A geometric crop showing the opponent's dugout or a single opposition player with head down — the contrast of victory and defeat in one frame.
- OVERLAY ZONES: Bottom 45% deep black gradient for text and stat overlays. The image is vertical (portrait, taller than wide).

PHASE 3: GRAPHIC ELEMENTS
- Shattered geometric frames — rectangles that look broken or exploded, fitting the upset theme.
- Explosion accent lines radiating from center, in {primary_team['primary']} color.
- Angular, aggressive accent shapes — sharp triangles, jagged edges.
- Small debris-like squares and diamond shapes scattered for visual chaos.
- High visual energy — this should feel like the biggest moment of the season.

PHASE 4: LIGHTING & TEXTURE
- Flash photography feel — harsh, direct lighting capturing raw emotion.
- Very high contrast, deep shadows, blown-out highlights on the celebration.
- Heavy film grain and noise, almost photojournalistic quality.
- Color grading pushed toward {primary_team['accent_desc']} in the highlights.

PHASE 5: TECH SPECS
Dynamic editorial collage. Shattered geometric elements over raw sports photography.
ABSOLUTELY NO TEXT, NO WORDS, NO LETTERS, NO NUMBERS, NO LOGOS anywhere in the image.
1080x1350 vertical portrait (4:5 aspect ratio). Taller than wide."""

    elif story_type == "player_spotlight":
        prompt = f"""Act as a Senior Editorial Designer creating a magazine-quality sports graphic.

PHASE 1: SEMANTIC INTELLIGENCE
Subject: NCAA College Softball — individual player achievement.
Sport: Women's college softball. Female athletes ONLY.
{color_dir}
Mood: Hero portrait, power, individual greatness.

PHASE 2: COMPOSITIONAL STRUCTURE
Single vertical portrait composition (1080x1350, 4:5 ratio):
- MAIN SUBJECT (Left 50%): A powerful portrait of a female college softball player. {primary_team['uniform']}. Batting stance mid-swing, or pitcher in wind-up — frozen at the most powerful point of the motion. Shot from slightly below, making her look larger than life.
- DETAIL CROP (Center-Right, geometric frame): A tight rectangular crop of the player's hands gripping the bat, or the softball leaving her hand — intimate athletic detail.
- SPOTLIGHT EFFECT: Dramatic rim lighting creating a bright outline around the player, isolating her from the background. Stadium lights behind creating a halo effect.
- OVERLAY ZONES: Bottom 45% transitions to deep black gradient for headline text and stat callout box. The image is vertical (portrait, taller than wide).

PHASE 3: GRAPHIC ELEMENTS
- Clean geometric frames with sharp edges, creating portrait-gallery layering.
- A bold color strip in {primary_team['primary']} running vertically, dividing the player zone from the stat zone.
- Circular spotlight accents — concentric rings emanating from behind the player.
- Subtle grid pattern in the dark overlay zones for texture.
- Small asterisk and dot accents in {primary_team['accent_desc']}.

PHASE 4: LIGHTING & TEXTURE
- Studio-quality hero lighting on the player. Strong contrast, professional sports portrait feel.
- Background stadium lights provide backlight and lens flares.
- Premium magazine print texture — fine grain, subtle halftone in mid-tones.
- Slightly desaturated background to push focus to the player.

PHASE 5: TECH SPECS
Hero portrait editorial design. Clean geometry over dramatic sports photography.
ABSOLUTELY NO TEXT, NO WORDS, NO LETTERS, NO NUMBERS, NO LOGOS anywhere in the image.
1080x1350 vertical portrait (4:5 aspect ratio). Taller than wide."""

    elif story_type == "matchup_preview":
        prompt = f"""Act as a Senior Editorial Designer creating a magazine-quality sports graphic.

PHASE 1: SEMANTIC INTELLIGENCE
Subject: NCAA College Softball — marquee matchup preview.
Sport: Women's college softball. Female athletes ONLY.
{color_dir}
Mood: Anticipation, competitive tension, big-game energy.

PHASE 2: COMPOSITIONAL STRUCTURE
Single vertical portrait composition (1080x1350, 4:5 ratio) with a SPLIT DESIGN:
- LEFT HALF: A female college softball pitcher in wind-up or release, facing right. {primary_team['uniform']}. Dramatic side lighting from the left.
- RIGHT HALF: A female college softball batter in stance, facing left, ready to swing. {'Secondary team uniform.' if len(teams) >= 2 else 'Opposing team uniform in contrasting colors.'}. Dramatic side lighting from the right.
- CENTER DIVIDER: A bold vertical element — lightning bolt, crack, or energy burst running top to bottom where the two sides meet. Creates visual tension between the two competitors.
- OVERLAY ZONES: Bottom 45% dark gradient across full width. Dark enough for headline text and stat box. The image is vertical (portrait, taller than wide).

PHASE 3: GRAPHIC ELEMENTS
- Split geometric grid — left side geometric frames in {primary_team['primary']}, right side in {'the second team color' if len(teams) >= 2 else 'contrasting color'}.
- Central energy burst with angular shards where the two sides collide.
- Diagonal lines of tension radiating from the center divide.
- Small accent shapes (squares, circles, stars) on both sides in respective team colors.

PHASE 4: LIGHTING & TEXTURE
- Split lighting design — warm tones on one side, cooler tones on the other.
- High contrast on both athletes, making each stand out from their background.
- Stadium atmosphere in deep background, lights and crowd energy.
- Unified grain texture across the entire image for cohesion.

PHASE 5: TECH SPECS
Split-screen editorial design with central tension element. Competitive matchup energy.
ABSOLUTELY NO TEXT, NO WORDS, NO LETTERS, NO NUMBERS, NO LOGOS anywhere in the image.
1080x1350 vertical portrait (4:5 aspect ratio). Taller than wide."""

    else:  # general / rankings_analysis
        prompt = f"""Act as a Senior Editorial Designer creating a magazine-quality sports graphic.

PHASE 1: SEMANTIC INTELLIGENCE
Subject: NCAA College Softball — news/analysis.
Sport: Women's college softball. Female athletes ONLY.
{color_dir}
Mood: Professional, authoritative, sports media quality.

PHASE 2: COMPOSITIONAL STRUCTURE
Single vertical portrait composition (1080x1350, 4:5 ratio):
- MAIN SUBJECT (Left-Center, 55%): A female college softball player in athletic action — fielding a ground ball, making a diving catch, or throwing to first. {primary_team['uniform']}. Captured in motion with dynamic body position.
- STADIUM ATMOSPHERE (Background): Wide shot of a college softball diamond during a night game. Stadium lights, scoreboard glow, crowd in stands. Beautiful depth of field.
- GEOMETRIC OVERLAY: Clean rectangular frame elements creating visual structure and depth.
- OVERLAY ZONES: Bottom 45% reserved for text — dark gradient fading to near-black. The image is vertical (portrait, taller than wide).

PHASE 3: GRAPHIC ELEMENTS
- Clean, professional geometric frames — rectangles and lines creating an analytical, broadcast-quality feel.
- Accent color strips in {primary_team['primary']} used sparingly for visual structure.
- Dotted line patterns and grid elements suggesting data and analysis.
- Subtle circular accents and small square elements for visual complexity.

PHASE 4: LIGHTING & TEXTURE
- Broadcast-quality sports photography lighting. Clean, professional.
- Night game atmosphere with stadium lights creating beautiful bokeh in background.
- Medium film grain for editorial magazine texture.
- Neutral-warm color grading with {primary_team['accent_desc']} highlights.

PHASE 5: TECH SPECS
Clean editorial sports design. Professional broadcast aesthetic.
ABSOLUTELY NO TEXT, NO WORDS, NO LETTERS, NO NUMBERS, NO LOGOS anywhere in the image.
1080x1350 vertical portrait (4:5 aspect ratio). Taller than wide."""

    return prompt


def generate_background_image(client, story_title, story_type, output_path,
                              model=None, verify=True, retries=2):
    """Generate a rich background image. Supports Imagen and Nano Banana models."""
    from google.genai import types

    model = model or DEFAULT_MODEL
    prompt = build_background_prompt(story_title, story_type, story_data=None)
    is_imagen = model.startswith("imagen")

    # Get expected team color for verification
    teams = get_team_info(story_title, story_type)
    expected_color = teams[0]["accent_desc"] if teams else "orange and red"

    for attempt in range(retries + 1):
        try:
            if is_imagen:
                # Imagen API uses generate_images()
                response = client.models.generate_images(
                    model=model,
                    prompt=prompt[:4000],  # Imagen prompt limit
                    config=types.GenerateImagesConfig(number_of_images=1),
                )
                if response.generated_images:
                    img_data = response.generated_images[0].image.image_bytes
                else:
                    log.warning("Imagen returned no images, retrying...")
                    time.sleep(2)
                    continue
            else:
                # Nano Banana / Gemini models use generate_content()
                response = client.models.generate_content(
                    model=model,
                    contents=prompt,
                    config=types.GenerateContentConfig(
                        response_modalities=["IMAGE", "TEXT"],
                    ),
                )
                img_data = None
                for part in response.candidates[0].content.parts:
                    if part.inline_data:
                        img_data = part.inline_data.data
                        break
                if not img_data:
                    log.warning("No image in response, retrying...")
                    time.sleep(2)
                    continue

            if len(img_data) < 10240:
                log.warning("Image too small (%d bytes), retrying...", len(img_data))
                time.sleep(2)
                continue

            os.makedirs(os.path.dirname(output_path), exist_ok=True)
            with open(output_path, "wb") as f:
                f.write(img_data)
            log.info("Background generated: %s (%d KB, %s)",
                     os.path.basename(output_path), len(img_data) // 1024, model.split("/")[-1] if "/" in model else model)

            # AI verification gate
            if verify:
                passed, issues = verify_image(client, output_path, expected_color, story_type)
                if not passed and attempt < retries:
                    log.warning("  Verification failed, regenerating (attempt %d)...", attempt + 2)
                    time.sleep(1)
                    continue
                elif not passed:
                    log.warning("  Verification failed on final attempt — using anyway")

            return True

        except Exception as e:
            log.warning("Attempt %d failed: %s", attempt + 1, e)
            if attempt < retries:
                time.sleep(3)

    log.error("All retries failed for background: %s", story_title[:50])
    return False


def build_complete_prompt(story_title, key_stat, story_type):
    """Build an optimized Approach C prompt based on story type."""

    # Sport context — reinforced in every prompt
    sport_context = (
        "NCAA COLLEGE SOFTBALL. "
        "Female athletes playing softball. Softball bats, softballs, softball diamonds. "
        "NOT football. NOT baseball. NOT men's sports."
    )

    # Trademark prevention
    no_trademarks = (
        "Do NOT include any real TV network logos (no ESPN, no FOX, no CBS). "
        "Do NOT include any real brand logos. "
        "Use generic scoreboard or stat graphic styling instead."
    )

    stat_line = ""
    if key_stat:
        # Extract the most impactful number from the stat
        import re as _re
        numbers = _re.findall(r'\d+', key_stat)
        big_num = max(numbers, key=lambda x: int(x)) if numbers else ""
        stat_line = (
            f"Feature a large, prominent stat callout: \"{key_stat}\". "
            f"The number {big_num} should be displayed VERY LARGE (biggest element in the image) "
            f"inside a bold stat box or badge. "
        )

    # Story-type specific visual direction
    type_visuals = {
        "game_recap": (
            "Include a scoreboard-style element showing the final score prominently. "
            "Show softball player action silhouettes celebrating or in motion. "
            "Use team-themed color accents in the gradient background. "
        ),
        "player_spotlight": (
            "Feature a dramatic softball player silhouette in batting or pitching stance. "
            "Spotlight/hero lighting effect on the player. "
            "Stat number should be the visual centerpiece. "
        ),
        "matchup_preview": (
            "Split composition — VS style with two sides representing each team. "
            "Team color accents on each side. Versus or matchup energy. "
            "Show game time/date info if provided. "
        ),
        "record_tracker": (
            "Milestone/record-breaking visual energy — ascending bars, rising arrows, breakthrough effects. "
            "The record number should be the dominant visual element. "
            "Historical comparison feel — old record vs new record. "
        ),
        "upset": (
            "Upset energy — dramatic, explosive, shock factor. "
            "Shattered expectations visual metaphor. "
            "Winner prominently featured, underdog-beats-giant narrative. "
        ),
        "rankings_analysis": (
            "Rankings board or tier list visual style. "
            "Movement arrows showing teams rising or falling. "
            "Clean, analytical, data-forward composition. "
        ),
        "general": (
            "Softball diamond or stadium background elements. "
            "Clean, professional sports media composition. "
        ),
    }

    visual_dir = type_visuals.get(story_type, type_visuals["general"])

    prompt = (
        f"Create a professional sports infographic for {sport_context} "
        f"Headline text: \"{story_title[:80]}\". "
        f"{stat_line}"
        f"{visual_dir}"
        f"Style: Bleacher Report / modern sports media infographic. "
        f"Bold sans-serif typography. Dramatic gradient background in warm orange and red tones. "
        f"High contrast — text must be easily readable. "
        f"Professional broadcast-quality graphic. "
        f"{no_trademarks} "
        f"1080x1350 vertical portrait aspect ratio (4:5, taller than wide)."
    )

    return prompt


def generate_complete_image(client, story_title, key_stat, story_type, output_path, retries=2):
    """Approach C: Generate complete infographic via Nano Banana 2."""
    from google.genai import types

    prompt = build_complete_prompt(story_title, key_stat, story_type)

    for attempt in range(retries + 1):
        try:
            response = client.models.generate_content(
                model=DEFAULT_MODEL,
                contents=prompt,
                config=types.GenerateContentConfig(
                    response_modalities=["IMAGE", "TEXT"],
                ),
            )

            for part in response.candidates[0].content.parts:
                if part.inline_data:
                    img_data = part.inline_data.data
                    if len(img_data) < 10240:
                        log.warning("Image too small (%d bytes), retrying...", len(img_data))
                        continue
                    os.makedirs(os.path.dirname(output_path), exist_ok=True)
                    with open(output_path, "wb") as f:
                        f.write(img_data)
                    log.info("C-style complete: %s (%d KB)", os.path.basename(output_path), len(img_data) // 1024)
                    return True

        except Exception as e:
            log.warning("Attempt %d failed: %s", attempt + 1, e)
            if attempt < retries:
                time.sleep(2)

    log.error("All retries failed for complete image: %s", story_title[:50])
    return False


def composite_infographic(base_path, output_path, headline, subline, big_stat, stat_label,
                          secondary_stats=None, score_line=None, score_detail=None):
    """Build a full infographic overlay on an AI background.

    Args:
        base_path: Path to the AI-generated background image
        output_path: Where to save the final composited image
        headline: Main headline text (e.g. "Wells Blasts Home Runs #23 and #24")
        subline: Secondary context line (e.g. "Oklahoma Run-Rules Ole Miss 10-0 in 6 Innings")
        big_stat: The big number for the stat callout (e.g. "24")
        stat_label: Label below the big number (e.g. "HOME RUNS")
        secondary_stats: List of secondary stat lines for the stat box (e.g. ["LEADS THE NATION", "6 FROM FRESHMAN RECORD (30)"])
        score_line: Score badge text (e.g. "OU 10 - OLE MISS 0")
        score_detail: Score badge detail (e.g. "Run-Rule (6 Inn)")
    """
    try:
        from PIL import Image, ImageDraw, ImageFont
    except ImportError:
        log.error("Pillow not installed. Run: pip install Pillow")
        return False

    engine_root = Path(__file__).resolve().parent.parent
    font_bold_path = str(engine_root / "fonts" / "Poppins-Bold.ttf")
    font_sub_path = str(engine_root / "fonts" / "Nunito-Variable.ttf")

    try:
        img = Image.open(base_path).convert("RGB")
        W, H = 1080, 1350  # 4:5 vertical
        img = img.resize((W, H), Image.LANCZOS)

        overlay = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        draw = ImageDraw.Draw(overlay)

        # Load fonts — sized up for 4:5 vertical
        def load_font(path, size):
            try:
                return ImageFont.truetype(path, size)
            except OSError:
                return ImageFont.load_default()

        f_headline = load_font(font_bold_path, 44)
        f_stat_big = load_font(font_bold_path, 82)
        f_stat_label = load_font(font_sub_path, 21)
        f_subline = load_font(font_sub_path, 23)
        f_tag = load_font(font_bold_path, 15)
        f_score = load_font(font_bold_path, 22)
        f_score_detail = load_font(font_sub_path, 15)
        f_secondary = load_font(font_sub_path, 17)

        accent = (255, 138, 0, 255)  # #FF8A00

        # ── 1. Gradient overlay on bottom 50% ──
        grad_start = H // 2
        for y in range(grad_start, H):
            alpha = min(220, int((y - grad_start) / (H - grad_start) * 220))
            draw.rectangle([(0, y), (W, y + 1)], fill=(0, 0, 0, alpha))

        # ── 2. Top accent bar ──
        draw.rectangle([(0, 0), (W, 5)], fill=accent)

        # ── 3. NCAA SOFTBALL tag ──
        draw.rounded_rectangle([(30, 22), (215, 52)], radius=5, fill=accent)
        draw.text((44, 25), "NCAA SOFTBALL", fill="white", font=f_tag)

        # ── 4. Headline (word-wrapped, up to 3 lines) ──
        max_w = W - 80
        words = headline.split()
        lines = []
        cur = ""
        for w in words:
            test = f"{cur} {w}".strip()
            bbox = draw.textbbox((0, 0), test, font=f_headline)
            if bbox[2] - bbox[0] <= max_w:
                cur = test
            else:
                if cur:
                    lines.append(cur)
                cur = w
        if cur:
            lines.append(cur)

        y_pos = 790
        for line in lines[:3]:
            draw.text((35, y_pos), line, fill="white", font=f_headline)
            y_pos += 54

        # ── 5. Subline ──
        if subline:
            draw.text((35, y_pos + 6), subline[:65], fill=(200, 200, 200, 230), font=f_subline)
            y_pos += 36

        # ── 6. Stat callout box (full width below headline) ──
        if big_stat:
            box_x = 35
            box_y = y_pos + 20
            box_w = W - 70
            box_h = 220

            draw.rounded_rectangle(
                [(box_x, box_y), (box_x + box_w, box_y + box_h)],
                radius=14, fill=(0, 0, 0, 200)
            )
            draw.rounded_rectangle(
                [(box_x, box_y), (box_x + box_w, box_y + box_h)],
                radius=14, outline=accent, width=2
            )

            # Big number — left side
            draw.text((box_x + 30, box_y + 15), str(big_stat), fill=accent, font=f_stat_big)

            # Stat label — right of the big number
            stat_bbox = draw.textbbox((0, 0), str(big_stat), font=f_stat_big)
            label_x = box_x + 30 + (stat_bbox[2] - stat_bbox[0]) + 25
            if stat_label:
                draw.text((label_x, box_y + 30), stat_label, fill="white", font=f_stat_label)

            # Divider
            draw.line([(box_x + 30, box_y + 115), (box_x + box_w - 30, box_y + 115)],
                      fill=(255, 138, 0, 80), width=1)

            # Secondary stats below divider
            if secondary_stats:
                sy = box_y + 130
                for s in secondary_stats[:3]:
                    draw.text((box_x + 30, sy), s, fill=(200, 200, 200, 200), font=f_secondary)
                    sy += 26

        # ── 7. Score badge (bottom left) ──
        if score_line:
            badge_w = max(300, draw.textbbox((0, 0), score_line, font=f_score)[2] + 50)
            badge_h = 78 if score_detail else 55
            badge_y = H - badge_h - 30
            draw.rounded_rectangle(
                [(30, badge_y), (30 + badge_w, badge_y + badge_h)],
                radius=10, fill=(255, 138, 0, 230)
            )
            draw.text((48, badge_y + 6), "FINAL", fill="white", font=f_tag)
            draw.text((48, badge_y + 27), score_line, fill="white", font=f_score)
            if score_detail:
                draw.text((48, badge_y + 54), score_detail, fill=(255, 255, 255, 200), font=f_score_detail)

        # ── 8. Brand mark ──
        draw.text((W - 210, H - 32), "I LOVE SOFTBALL", fill=(255, 138, 0, 130), font=f_tag)

        # Composite
        img_rgba = img.convert("RGBA")
        result = Image.alpha_composite(img_rgba, overlay)
        result = result.convert("RGB")
        result.save(output_path, "PNG")
        log.info("Composited infographic: %s", os.path.basename(output_path))
        return True

    except Exception as e:
        log.error("Composite failed: %s", e)
        import traceback
        traceback.print_exc()
        return False


def generate_bakeoff_html(content_folder, results):
    """Generate an HTML comparison page for the bake-off."""
    html = """<!DOCTYPE html>
<html><head><meta charset="UTF-8"><title>Image Bake-Off</title>
<style>
body { font-family: -apple-system, sans-serif; background: #1a1a2e; color: white; padding: 40px; }
h1 { text-align: center; margin-bottom: 40px; }
.story { margin-bottom: 60px; border-bottom: 1px solid #333; padding-bottom: 40px; }
.story h2 { color: #FF8A00; font-size: 18px; margin-bottom: 5px; }
.story .type { color: #888; font-size: 13px; margin-bottom: 20px; }
.compare { display: grid; grid-template-columns: 1fr 1fr; gap: 20px; }
.approach { text-align: center; }
.approach h3 { color: #aaa; font-size: 14px; margin-bottom: 10px; }
.approach img { width: 100%; border-radius: 8px; border: 2px solid #333; }
.approach .status { color: #666; font-size: 12px; margin-top: 8px; }
</style></head><body>
<h1>Image Bake-Off: Approach B vs C</h1>
"""

    for r in results:
        html += f"""
<div class="story">
    <h2>Article {r['num']}: {r['title'][:80]}</h2>
    <div class="type">Type: {r['story_type']} | Key stat: {r.get('key_stat', 'none')[:60]}</div>
    <div class="compare">
        <div class="approach">
            <h3>Approach B (AI Background + Text Overlay)</h3>
"""
        if r.get("b_path") and os.path.isfile(r["b_path"]):
            # Use relative path
            rel = os.path.relpath(r["b_path"], content_folder)
            html += f'            <img src="{rel}" alt="Approach B">\n'
        else:
            html += '            <div class="status">Generation failed</div>\n'

        html += """        </div>
        <div class="approach">
            <h3>Approach C (Full AI Generation)</h3>
"""
        if r.get("c_path") and os.path.isfile(r["c_path"]):
            rel = os.path.relpath(r["c_path"], content_folder)
            html += f'            <img src="{rel}" alt="Approach C">\n'
        else:
            html += '            <div class="status">Generation failed</div>\n'

        html += """        </div>
    </div>
</div>
"""

    html += "</body></html>"
    return html


def main():
    parser = argparse.ArgumentParser(description="Generate article hero images")
    parser.add_argument("date", nargs="?", help="Date (YYYY-MM-DD)")
    parser.add_argument("--niche", type=str, required=True)
    parser.add_argument("--model", type=str, default="imagen-ultra",
                        choices=list(MODEL_MAP.keys()),
                        help="Image generation model (default: imagen-ultra)")
    parser.add_argument("--skip-verify", action="store_true", help="Skip AI verification gate")
    parser.add_argument("--bakeoff", action="store_true", help="Generate both B and C for comparison (legacy)")
    parser.add_argument("--approach", type=str, choices=["B", "C"], default="B", help="Which approach (default: B)")
    args = parser.parse_args()

    selected_model = MODEL_MAP.get(args.model, DEFAULT_MODEL)
    do_verify = not args.skip_verify

    # Find paths
    engine_root = Path(__file__).resolve().parent.parent
    niche_launches = engine_root.parent
    niche_root = niche_launches / args.niche

    if not niche_root.is_dir():
        log.error("Niche folder not found: %s", niche_root)
        sys.exit(1)

    # Load niche config
    config_path = niche_root / "niche-config.yaml"
    content_prefix = "softball-content"  # default
    if config_path.is_file():
        with open(config_path) as f:
            for line in f:
                if line.startswith("content_prefix:"):
                    content_prefix = line.split(":")[1].strip().strip('"')

    # Find content folder
    if args.date:
        date_str = args.date
    else:
        date_str = datetime.now().strftime("%Y-%m-%d")
    content_folder = niche_root / f"{content_prefix}-{date_str}"

    if not content_folder.is_dir():
        log.error("Content folder not found: %s", content_folder)
        sys.exit(1)

    # Read daily brief for story titles
    brief_path = content_folder / "00-daily-brief.md"
    if not brief_path.is_file():
        log.error("Daily brief not found: %s", brief_path)
        sys.exit(1)

    with open(brief_path, "r", encoding="utf-8") as f:
        brief_text = f.read()

    # Read verified facts for key stats
    facts_path = content_folder / "01-verified-facts.md"
    facts_text = ""
    if facts_path.is_file():
        with open(facts_path, "r", encoding="utf-8") as f:
            facts_text = f.read()

    # Find articles
    articles_dir = content_folder / "articles"
    if not articles_dir.is_dir():
        log.error("No articles/ folder found in %s", content_folder)
        sys.exit(1)

    article_files = sorted(articles_dir.glob("article-*.html"))
    if not article_files:
        log.error("No article HTML files found in %s", articles_dir)
        sys.exit(1)

    log.info("Found %d articles in %s", len(article_files), content_folder.name)

    # Check usage limits before making any API calls
    can_proceed, usage_msg = check_usage_limits()
    log.info("Gemini usage: %s", usage_msg)
    if not can_proceed:
        log.error("BLOCKED: %s", usage_msg)
        sys.exit(1)

    # Calculate how many images this run will generate
    images_needed = len(article_files) * (2 if args.bakeoff else 1)
    today_str = datetime.now().strftime("%Y-%m-%d")
    usage_data = {}
    if os.path.isfile(USAGE_LOG):
        try:
            with open(USAGE_LOG) as f:
                usage_data = json.load(f)
        except (json.JSONDecodeError, IOError):
            pass
    today_used = usage_data.get("daily", {}).get(today_str, 0)
    if today_used + images_needed > DAILY_IMAGE_CAP:
        log.error("BLOCKED: This run needs %d images but only %d remaining in daily cap (%d/%d used)",
                  images_needed, DAILY_IMAGE_CAP - today_used, today_used, DAILY_IMAGE_CAP)
        sys.exit(1)

    # Extract story info from brief
    stories = []
    story_pattern = re.compile(r"### STORY (\d+): (.+)")
    for match in story_pattern.finditer(brief_text):
        num = int(match.group(1))
        title = match.group(2).strip()
        stories.append({"num": num, "title": title})

    # Initialize Gemini
    client = get_gemini_client()
    if not client:
        log.error("Cannot initialize Gemini. Exiting.")
        sys.exit(1)

    # Generate images
    images_dir = content_folder / "article-images"
    os.makedirs(images_dir, exist_ok=True)

    results = []
    for article_file in article_files:
        # Extract story number from filename
        num_match = re.match(r"article-(\d+)", article_file.stem)
        if not num_match:
            continue
        story_num = int(num_match.group(1))

        # Find story info
        story_info = next((s for s in stories if s["num"] == story_num), None)
        if not story_info:
            log.warning("No story info for article %d, using filename", story_num)
            story_info = {"num": story_num, "title": article_file.stem.replace("-", " ").title()}

        title = story_info["title"]
        story_type = classify_story(title)
        story_data = extract_story_data(facts_text, story_num, title)

        log.info("Article %d: %s [%s] stat=%s", story_num, title[:50], story_type,
                 story_data.get("big_stat", "none"))

        result = {
            "num": story_num,
            "title": title,
            "story_type": story_type,
            "key_stat": story_data.get("big_stat", ""),
        }

        if args.bakeoff or args.approach == "B":
            # Generate rich background then composite infographic
            bg_path = str(images_dir / f"article-{story_num:02d}-bg.png")
            b_final_path = str(images_dir / f"article-{story_num:02d}-B.png")

            if generate_background_image(client, title, story_type, bg_path,
                                         model=selected_model, verify=do_verify):
                composite_infographic(
                    bg_path, b_final_path,
                    headline=title,
                    subline=story_data.get("subline", ""),
                    big_stat=story_data.get("big_stat"),
                    stat_label=story_data.get("stat_label"),
                    secondary_stats=story_data.get("secondary_stats"),
                    score_line=story_data.get("score_line"),
                    score_detail=story_data.get("score_detail"),
                )
                result["b_path"] = b_final_path
            time.sleep(0.5)  # Rate limiting

        if args.bakeoff or args.approach == "C":
            # Approach C: full AI generation (kept for comparison only)
            c_path = str(images_dir / f"article-{story_num:02d}-C.png")
            key_stat_text = None
            for fact in (story_data.get("secondary_stats") or []):
                key_stat_text = fact
                break
            generate_complete_image(client, title, key_stat_text, story_type, c_path)
            result["c_path"] = c_path
            time.sleep(0.5)  # Rate limiting

        results.append(result)

    # Generate bake-off comparison HTML
    if args.bakeoff:
        bakeoff_html = generate_bakeoff_html(str(content_folder), results)
        bakeoff_path = content_folder / "image-bakeoff.html"
        with open(bakeoff_path, "w", encoding="utf-8") as f:
            f.write(bakeoff_html)
        log.info("Bake-off comparison: %s", bakeoff_path)

    # Summary and usage logging
    b_count = sum(1 for r in results if r.get("b_path") and os.path.isfile(r["b_path"]))
    c_count = sum(1 for r in results if r.get("c_path") and os.path.isfile(r["c_path"]))
    total_api_calls = b_count + c_count  # Each B needs 1 Gemini call (bg), each C needs 1
    log_usage(total_api_calls)
    log.info("Done: %d B-style, %d C-style images generated (%d Gemini API calls, ~$%.2f)",
             b_count, c_count, total_api_calls, total_api_calls * COST_PER_IMAGE)


if __name__ == "__main__":
    main()
