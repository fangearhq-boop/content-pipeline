# I Love Softball — Imagn Image Sourcing Workflow Guide

## Overview

This guide documents the image sourcing workflow using Imagn (USA TODAY Sports Images) for the I Love Softball daily content pipeline. The review dashboard generates clickable Imagn search links for each story's image concepts, making it easy to find and license the right photos.

---

## How It Works

### 1. Pipeline Generates Image Concepts
Each daily content run creates image concepts with:
- **Imagn Search Terms** — specific, pre-written search queries optimized for finding the right photos
- **Text Overlay Copy** — the text that will go over the photo in Canva
- **Caption** — the photo credit/caption text for social media

### 2. Review Dashboard Has Clickable Links
The review dashboard (`review-dashboard.html`) includes:
- **Blue pill buttons** for each Imagn search term — click to open Imagn search in a new tab
- **Dark navy preview boxes** showing text overlay copy in brand colors (gold headline, white sub-text)
- Each image concept card has 3-5 search term links

### 3. You Browse & Select Photos on Imagn
1. Open the review dashboard in your browser
2. Find the image concept card for the story you're working on
3. Click the blue Imagn search buttons — each opens imagn.com with the search pre-filled
4. Browse results, pick the best photo
5. Download/license the photo
6. Upload to Canva for graphic creation

---

## Imagn Site Navigation

### URL Format
```
https://www.imagn.com/search?q=SEARCH+TERMS
```

### Key Sections
- **Homepage:** imagn.com
- **Sports Browse:** imagn.com/sports/
- **Photo Galleries:** imagn.com/public-galleries/
- **Advanced Search:** Available from main navigation

### Search Tips for College Softball
- **Use player full names:** "Reese Atwood" works better than just "Atwood"
- **Include team + sport:** "Tennessee softball" narrows results
- **Add venue/event:** "Clearwater Invitational" helps find specific tournament photos
- **Include date range:** Use the date filter on Imagn to narrow to recent photos (last 7 days)
- **Try multiple terms:** The dashboard provides 3-5 search terms per story — try several to find the best options

### Licensing
- Imagn content is now licensed through Reuters
- Editorial use requires proper photo credit: "(USA TODAY Sports Images)"
- Contact Reuters for licensing inquiries

---

## Integration with Canva

### After Finding Photos on Imagn:
1. **Download** the selected photo from Imagn
2. **Open Canva** and create a new design (1200x675 for Twitter, 1200x630 for Facebook)
3. **Upload** the Imagn photo to your Canva design
4. **Apply Brand Kit** — use the I Love Softball brand kit (ID: kAGENnl7bLQ) for fonts and colors
5. **Add Text Overlay** — copy the overlay text from the dashboard's dark preview box
   - Headline: Bebas Neue font, Gold (#FFD700), uppercase
   - Sub-text: Montserrat font, White (#FFFFFF)
6. **Add Logo** — place the I Love Softball logo (softball with fireworks)
7. **Export** as PNG at 1200x675 (Twitter) or 1200x630 (Facebook)

### Brand Kit Quick Reference
| Element | Value |
|---------|-------|
| Title Font | Bebas Neue (bold, sporty) |
| Subtitle Font | Montserrat (clean, professional) |
| Body Font | Open Sans (readable) |
| Primary Orange | #FF8A00 |
| Primary Gold | #FFD700 |
| Accent Red | #E53935 |
| Dark Navy | #1A1A2E |
| White | #FFFFFF |
| Logo | i-love-softball-logo.jpg |
| Brand Kit ID | kAGENnl7bLQ |

---

## Daily Workflow Checklist

- [ ] Run the content pipeline (`softball-content-pipeline` skill)
- [ ] Open the review dashboard in browser
- [ ] Review and approve/edit content for each story
- [ ] For each approved story with images:
  - [ ] Click Imagn search links from dashboard
  - [ ] Select best photo from Imagn results
  - [ ] Download photo
  - [ ] Create Canva graphic with brand kit
  - [ ] Add text overlay from dashboard preview
  - [ ] Export final graphic
- [ ] Attach graphics to social posts
- [ ] Schedule posts in PostPlanner (export CSV from dashboard)
- [ ] Publish articles to WordPress

---

## Typical Imagn Search Terms by Story Type

### Player Performance Story
- `[Player Name] [Team] [Sport] [Year]`
- `[Player Name] [action: batting/pitching/celebration] [Year]`
- `[Player Name] [opponent] [venue] [date]`

### Game Recap
- `[Team A] vs [Team B] [venue] [date]`
- `[Team] celebration [event]`
- `[Team] softball [venue] [Year]`

### Preview/Matchup
- `[Player 1] [Team] pitcher [Year]` + `[Player 2] [Team] pitcher [Year]`
- `[Event/Tournament] [venue] [Year]`
- `[Team] softball [Year]` (general team action shots)

### Venue/Atmosphere
- `[Venue name] softball [Year]`
- `[Event] crowd fans [Year]`
- `college softball tournament atmosphere`

---

## Photo Selection Best Practices

1. **Action shots > posed shots** — Game action is more engaging than posed team photos
2. **Emotion matters** — Celebrations, intensity, drama tell the story visually
3. **Team colors prominent** — Make sure uniforms and team identity are clearly visible
4. **Clean backgrounds** — Avoid cluttered images that will fight with text overlay
5. **Face visibility** — For player-specific stories, make sure the player's face is visible and recognizable
6. **Horizontal orientation** — Social media graphics are landscape (1200x675), so horizontal photos work best
7. **High resolution** — Download the highest resolution available for crisp social media graphics
8. **Recency** — Use photos from the current season (2026) whenever possible

---

## Notes

- Imagn requires an account/subscription for downloading photos
- All photos must include proper credit: "(USA TODAY Sports Images)" or "(Imagn Images)"
- The review dashboard's Imagn links open in new tabs, so you can browse multiple searches simultaneously
- Text overlay previews in the dashboard show approximate styling — final Canva graphics may differ slightly
- The dashboard generates new Imagn links each time the pipeline runs, so links always match the day's stories
