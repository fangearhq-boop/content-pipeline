# FanGear HQ Content Engine: Daily Brief Format
**Universal Template** | Niche-specific values from: brand-guide.md, brand-voice.md, niche-config.yaml

---

## Daily Brief Header

```
# {BRAND_NAME} - Daily Brief
**Date:** {PUBLICATION_DATE}
**Timezone:** {CONFIG.timezone}
**Brief Prepared By:** FanGear HQ Content Engine
```

---

## Story Decision Matrix

| Story # | Title | Content Pillar | Freshness Tag | Tier | Platforms | Priority |
|---------|-------|-----------------|----------------|------|-----------|----------|
| 1 | {Title} | {Pillar} | {Tag} | {Tier} | {Platform List} | {1-10} |
| 2 | {Title} | {Pillar} | {Tag} | {Tier} | {Platform List} | {1-10} |

---

## Story Details

### STORY 1: {STORY_TITLE}
**Content Pillar:** {CONFIG.pillar_1} *(if niche uses pillars)*
**Freshness Tag:** BREAKING | TODAY | UPCOMING | EVERGREEN | TRENDING
**Tier:** 1 | 2 | 3
**Assigned Platforms:** {Based on tier rules}
**Priority Score:** {1-10}

**Summary (2-4 sentences):**
{Concise overview of story, why it matters to this audience, key hook}

---

### STORY 2-N: {ADDITIONAL_STORIES}
*(Follow same format as STORY 1)*

---

## Story Count Guidelines

- **Target:** 7 stories
- **Acceptable Range:** 5-8 stories
- **Minimum Distribution:**
  - Tier 1 (Breaking/Trending): 1-2 stories
  - Tier 2 (Today/Upcoming): 3-4 stories
  - Tier 3 (Evergreen): 1-2 stories

---

## Platform Assignment Rules by Tier

| Tier | Content Type | Platform Assignment |
|------|--------------|---------------------|
| **Tier 1** | Breaking/Trending | X + Facebook + {Optional: TikTok, Instagram} |
| **Tier 2** | Today/Upcoming | X + Facebook + {Optional: LinkedIn} |
| **Tier 3** | Evergreen | {Single platform or secondary channels} |

---

## Publishing Schedule

**Default Publishing Windows** (all times in {CONFIG.timezone}):

| Time Slot | Platform(s) | Content Type | Notes |
|-----------|-------------|--------------|-------|
| 8:00-9:00 AM | X + Facebook | Morning Brief Highlight | Tier 1/2 mix |
| 10:00-11:00 AM | {CONFIG.secondary_platform_1} | Mid-Morning Update | Secondary content |
| 12:00-1:00 PM | X + Facebook | Midday Brief | Quick updates |
| 3:00-4:00 PM | {CONFIG.secondary_platform_2} | Afternoon Deep Dive | Longer-form if applicable |
| 7:00-8:00 PM | X + Facebook | Evening Recap | Day summary |

**Notes:**
- All social posts MUST include a specific posting window
- Adjust timing based on {CONFIG.audience_peak_hours}
- Reserve flexibility for breaking news (Tier 1 stories may post immediately)

---

## Content Tone & Voice

**Brand Voice Guidelines:** *From {BRAND_NAME} brand-voice.md*
- {VOICE_CHARACTERISTIC_1}
- {VOICE_CHARACTERISTIC_2}
- {VOICE_CHARACTERISTIC_3}

**Hashtag Strategy:** *From {BRAND_NAME} brand-guide.md*
- Primary hashtag: {CONFIG.primary_hashtag}
- Secondary hashtags: {CONFIG.secondary_hashtags}

---

## Daily Brief Workflow Checklist

- [ ] All 5-8 stories identified and prioritized
- [ ] Each story assigned to appropriate tier (1/2/3)
- [ ] Platform assignments match tier rules
- [ ] All posting windows specified
- [ ] Summaries written with audience relevance
- [ ] Freshness tags accurately reflect story status
- [ ] Daily brief ready for research-notes phase
