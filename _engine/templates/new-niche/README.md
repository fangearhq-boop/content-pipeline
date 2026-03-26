# New Niche Setup — Step-by-Step Checklist

Use this guide to set up a new content niche in the FanGear HQ engine.
Every niche lives in its own folder under `Niche_Launches/` and plugs into
the shared 15-step pipeline at `_engine/SKILL.md`.

---

## Quick Start

1. Copy this entire `new-niche/` template folder to `Niche_Launches/{YourNiche}/`
2. Rename and fill in each file (see File Checklist below)
3. Create the GitHub Pages dashboard repo
4. Run the Verification section to confirm everything is wired up
5. Delete this README (or rename it) — the niche's own `CLAUDE.md` becomes the project rules file

---

## File Checklist

Create these files **in this order** — later files reference earlier ones.

| # | File | What It Does | Depends On |
|---|------|-------------|------------|
| 1 | `niche-config.yaml` | Core settings: brand name, platforms, schedule, photo source, article config, GitHub Pages URL. The engine reads this first. | Nothing |
| 2 | `brand-voice.md` | Personality, tone, style rules, terminology, platform-specific voice. Defines HOW you sound. | niche-config (brand name) |
| 3 | `brand-guide.md` | Visual identity: colors, fonts, image dimensions, composition rules, photo credit format. Defines HOW you look. | niche-config (photo source) |
| 4 | `seasonal-calendar.md` | Annual rhythm: what's happening when, how it affects story tiering. Drives research priorities. | brand-voice (to understand audience) |
| 5 | `api-reference.md` | Where to find content: news sources, data sources, community sources, stock photo sources. | seasonal-calendar (to know what events to source) |
| 6 | `research-playbook.md` | How to research this niche: categories, tiering criteria, posting priority, fact-check focus areas. | api-reference + seasonal-calendar |
| 7 | `claim-patterns.py` | Python module defining niche-specific fact-check claim types and priorities. Used by `verify-facts.py`. | research-playbook (fact-check focus areas) |
| 8 | `SKILL.md` | Thin skill file that reads `_engine/SKILL.md` and applies this niche's config. Entry point for the pipeline. | All of the above |
| 9 | `CLAUDE.md` | Project rules file with niche-specific overrides, Canva config, platform rules, verification checklist. | All of the above |
| 10 | `pipeline-status.md` | Cross-session state tracking. Initialize with "No runs yet." | Nothing |
| 11 | `story-history.md` | Running log of covered stories. Initialize empty with header only. | Nothing |

### Files provided in this template (1-6)

This template includes annotated skeletons for files 1-6 plus `research-playbook.md`.
Files 7-11 are niche-specific and must be created from scratch, but are simple:

- **`claim-patterns.py`** — Copy from an existing niche (e.g., Softball or Parenting) and adapt the claim types. The engine's `verify-facts.py` imports this module.
- **`SKILL.md`** — Follow the pattern from any existing niche. It's typically ~20 lines that read the engine SKILL.md and point to local config files.
- **`CLAUDE.md`** — Copy from an existing niche and replace brand-specific rules.
- **`pipeline-status.md`** — Just a markdown file with a header and "No pipeline runs yet."
- **`story-history.md`** — Just a markdown file with a header row.

---

## GitHub Pages Dashboard Setup

Each niche needs a GitHub repo for publishing review dashboards.

```bash
# 1. Create the repo
gh repo create fangearhq-boop/{NICHE_SHORT}-dashboards --private --clone

# 2. Initialize with .nojekyll (required for GitHub Pages)
cd {NICHE_SHORT}-dashboards
touch .nojekyll
git add .nojekyll
git commit -m "Initialize dashboard repo"
git push

# 3. Enable GitHub Pages (workflow mode)
#    publish-dashboard.py handles this automatically on first run,
#    but you can verify:
gh api repos/fangearhq-boop/{NICHE_SHORT}-dashboards/pages --jq '{build_type, status}'
```

Update `niche-config.yaml` with:
- `github_pages_url: "https://fangearhq-boop.github.io/{NICHE_SHORT}-dashboards/"`
- `github_repo: "fangearhq-boop/{NICHE_SHORT}-dashboards"`

---

## Canva Brand Kit Setup

1. Create a new Brand Kit in Canva with the niche's colors and fonts from `brand-guide.md`
2. Copy the Brand Kit ID from the Canva URL (format: `kXXXXXXXXXX`)
3. Add it to `niche-config.yaml` as `canva_brand_kit_id`

---

## Verification — Confirm the Niche Is Ready

Run these checks before the first pipeline run:

### 1. Config loads correctly
```bash
# From the niche folder, verify YAML is valid
python -c "import yaml; print(yaml.safe_load(open('niche-config.yaml'))['brand_name'])"
# Expected: Your brand name
```

### 2. All required files exist
```bash
# Check for the minimum file set
ls niche-config.yaml brand-voice.md brand-guide.md seasonal-calendar.md api-reference.md research-playbook.md SKILL.md CLAUDE.md claim-patterns.py pipeline-status.md story-history.md
# All 11 files should be listed with no errors
```

### 3. GitHub Pages repo is accessible
```bash
gh api repos/fangearhq-boop/{NICHE_SHORT}-dashboards/pages --jq '{build_type, status}'
# Expected: {"build_type":"workflow","status":"built"}
```

### 4. Claim patterns module imports cleanly
```bash
python -c "import claim_patterns; print(claim_patterns.CLAIM_TYPES)"
# Expected: Dictionary of claim types with priority levels
```

### 5. Photo source is configured
- **imagn**: Verify Imagn login works at imagn.com
- **stock**: No setup needed (Unsplash/Pexels are free)
- **gemini**: Verify `GEMINI_API_KEY` env var is set

### 6. Dry-run the pipeline
```bash
# Run Step 1 (research) only to confirm web search works for this niche
# Then verify the output folder was created:
ls {CONTENT_PREFIX}-$(date +%Y-%m-%d)/
```

---

## Common Pitfalls

- **Forgot to update `content_prefix`** — All content folders use this prefix. If it doesn't match, scripts can't find your content.
- **Wrong `photo_source`** — Using `imagn` for a non-sports niche means no photos will be found. Use `stock` or `gemini` for non-sports.
- **Missing `claim-patterns.py`** — The fact-check step (Step 10) imports this module. Without it, fact-checking fails silently.
- **GitHub Pages on legacy Jekyll** — Must be workflow mode. `publish-dashboard.py` handles this, but check if it fails.
- **Timezone mismatch** — `default_schedule` times are in the timezone specified in `niche-config.yaml`. Posting tools convert to UTC. Make sure they match your audience's timezone.
