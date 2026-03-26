# FanGear HQ Content Engine: X/Twitter Posts Format
**Universal Template** | Niche-specific values from: brand-guide.md, brand-voice.md, niche-config.yaml

---

## File Header

```
# {BRAND_NAME} - X Posts
**Date:** {POSTING_DATE}
**Prepared By:** FanGear HQ Content Engine
```

---

## Per-Story Format

Repeat this block for each story (1 through N). Each story gets 1-2 text posts (different angles). Stories with images also get an image post.

### STORY {N}: {STORY_TITLE}

#### Text Post — {POSTING_WINDOW}

```
{Hook — 1-2 punchy sentences with the key stat or headline.}

{Detail — context, supporting info, or the take. 1-2 sentences.}

{#Hashtag1 #Hashtag2 #Hashtag3}
```

**Spacing rules:** Use blank lines to create visual breathing room. Always separate: (1) the hook from the detail, and (2) the hashtags from the body. Newlines count as 1 character each toward 280.

**Character count:** Do NOT put `[CHARACTER COUNT: XX/280]` tags inside code blocks — they inflate the real tweet length and will appear as tweet text. The `verify-facts.py` script (Step 10) calculates accurate counts automatically. If you need a reference count, place it *outside* the code block as a markdown note.

#### Image Post — {POSTING_WINDOW}

```
{Short caption text, 100-150 characters}
```

---

## Post Schedule Summary

| Time | Stories | Post Type | Count |
|------|---------|-----------|-------|
| {TIME} | {Story #s} | {Type} | {N} |

**Total Daily X Posts:** {N}

---

## Reminders (for content engine, not included in output)

- X post limit: 280 characters including spaces, punctuation, hashtags
- URLs count as 23 characters
- Max 3 hashtags per post
- Max 1 emoji per post (from approved list in brand-voice.md)
- Brand voice reference: brand-voice.md
- Posting times from niche-config.yaml default_schedule
