#!/usr/bin/env python3
"""
Fetch Reddit Sentiment — Chicago Cubs Fan HQ

Pulls top/hot posts from r/CHICubs (and optionally r/baseball Cubs mentions)
using Reddit's public JSON API. No authentication required.

Outputs a markdown file that feeds into the pipeline's Step 1 research.

Usage:
    python fetch-reddit-sentiment.py                    # defaults: hot posts, 25 limit
    python fetch-reddit-sentiment.py --sort top --time day --limit 30
    python fetch-reddit-sentiment.py --include-rbaseball  # also search r/baseball
    python fetch-reddit-sentiment.py --output custom-file.md

Output: reddit-sentiment-YYYY-MM-DD.md in the current directory (or dated content folder)
"""

import argparse
import io
import json
import sys
import urllib.request
import urllib.error
from datetime import datetime, timezone

# Fix Windows console encoding for emoji/unicode
if sys.platform == "win32":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8", errors="replace")


# Reddit public JSON API — no auth needed for read-only access
REDDIT_BASE = "https://www.reddit.com"
USER_AGENT = "FanGearHQ-CubsSentiment/1.0 (content research tool)"

# Subreddits to scan
PRIMARY_SUB = "CHICubs"
SECONDARY_SUB = "baseball"

# Keywords to filter r/baseball for Cubs-relevant posts
CUBS_KEYWORDS = [
    "cubs", "chicago cubs", "wrigley", "wrigleyville",
    # Add current roster names as needed
    "marquee sports",
]


def fetch_subreddit(subreddit, sort="hot", time_filter="day", limit=25):
    """Fetch posts from a subreddit using Reddit's public JSON API.

    Args:
        subreddit: Subreddit name (without r/)
        sort: "hot", "top", "new", "rising"
        time_filter: For "top" sort — "hour", "day", "week", "month", "year", "all"
        limit: Number of posts to fetch (max 100)

    Returns:
        List of post dicts with title, score, num_comments, url, selftext, created_utc
    """
    if sort == "top":
        url = f"{REDDIT_BASE}/r/{subreddit}/top.json?t={time_filter}&limit={limit}"
    else:
        url = f"{REDDIT_BASE}/r/{subreddit}/{sort}.json?limit={limit}"

    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})

    try:
        with urllib.request.urlopen(req, timeout=15) as response:
            data = json.loads(response.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        print(f"  ⚠ HTTP {e.code} fetching r/{subreddit}/{sort}: {e.reason}")
        return []
    except urllib.error.URLError as e:
        print(f"  ⚠ Network error fetching r/{subreddit}/{sort}: {e.reason}")
        return []
    except Exception as e:
        print(f"  ⚠ Error fetching r/{subreddit}/{sort}: {e}")
        return []

    posts = []
    for child in data.get("data", {}).get("children", []):
        p = child.get("data", {})
        posts.append({
            "title": p.get("title", ""),
            "score": p.get("score", 0),
            "num_comments": p.get("num_comments", 0),
            "url": f"https://reddit.com{p.get('permalink', '')}",
            "selftext": (p.get("selftext", "") or "")[:500],  # truncate long posts
            "created_utc": p.get("created_utc", 0),
            "link_flair_text": p.get("link_flair_text", ""),
            "author": p.get("author", "[deleted]"),
            "is_self": p.get("is_self", False),
            "upvote_ratio": p.get("upvote_ratio", 0),
        })

    return posts


def filter_cubs_posts(posts):
    """Filter r/baseball posts to only Cubs-relevant ones."""
    filtered = []
    for p in posts:
        text = (p["title"] + " " + p.get("selftext", "")).lower()
        if any(kw in text for kw in CUBS_KEYWORDS):
            filtered.append(p)
    return filtered


def calculate_sentiment_signal(posts):
    """Simple heuristic sentiment from post engagement patterns.

    Returns a dict with overall mood indicators.
    """
    if not posts:
        return {"mood": "unknown", "energy": "low", "top_themes": []}

    total_score = sum(p["score"] for p in posts)
    total_comments = sum(p["num_comments"] for p in posts)
    avg_ratio = sum(p["upvote_ratio"] for p in posts) / len(posts)

    # High comments relative to upvotes = controversy/debate
    # High upvotes with high ratio = consensus/excitement
    energy = "high" if total_comments > len(posts) * 50 else "moderate" if total_comments > len(posts) * 15 else "low"

    if avg_ratio > 0.85:
        mood = "positive/united"
    elif avg_ratio > 0.70:
        mood = "mixed/debating"
    else:
        mood = "frustrated/divided"

    # Extract common flair themes
    flairs = [p["link_flair_text"] for p in posts if p["link_flair_text"]]
    top_flairs = list(set(flairs))[:5]

    return {
        "mood": mood,
        "energy": energy,
        "total_score": total_score,
        "total_comments": total_comments,
        "avg_upvote_ratio": round(avg_ratio, 2),
        "post_count": len(posts),
        "top_flairs": top_flairs,
    }


def format_post_markdown(post, index):
    """Format a single post as markdown."""
    age_hours = (datetime.now(timezone.utc).timestamp() - post["created_utc"]) / 3600
    age_str = f"{age_hours:.0f}h ago" if age_hours < 48 else f"{age_hours/24:.0f}d ago"

    flair = f" [{post['link_flair_text']}]" if post["link_flair_text"] else ""
    selftext = ""
    if post["selftext"] and post["is_self"]:
        preview = post["selftext"][:200].replace("\n", " ").strip()
        if len(post["selftext"]) > 200:
            preview += "..."
        selftext = f"\n  > {preview}"

    return (
        f"{index}. **{post['title']}**{flair}\n"
        f"   ↑{post['score']} | 💬 {post['num_comments']} | "
        f"ratio: {post['upvote_ratio']:.0%} | {age_str} | u/{post['author']}"
        f"{selftext}"
    )


def generate_markdown(chicubs_posts, baseball_posts, sentiment, args):
    """Generate the full markdown output."""
    today = datetime.now().strftime("%Y-%m-%d")
    time_now = datetime.now().strftime("%I:%M %p CT")

    lines = [
        f"# Reddit Fan Sentiment — {today}",
        f"",
        f"*Generated at {time_now} | "
        f"Source: r/{PRIMARY_SUB} ({args.sort}/{args.time}) | "
        f"Limit: {args.limit}*",
        f"",
        f"---",
        f"",
        f"## Sentiment Summary",
        f"",
        f"| Metric | Value |",
        f"|--------|-------|",
        f"| Overall Mood | **{sentiment['mood']}** |",
        f"| Fan Energy | **{sentiment['energy']}** |",
        f"| Posts Analyzed | {sentiment['post_count']} |",
        f"| Total Upvotes | {sentiment['total_score']:,} |",
        f"| Total Comments | {sentiment['total_comments']:,} |",
        f"| Avg Upvote Ratio | {sentiment['avg_upvote_ratio']:.0%} |",
    ]

    if sentiment["top_flairs"]:
        lines.append(f"| Active Flairs | {', '.join(sentiment['top_flairs'])} |")

    lines.extend([
        f"",
        f"---",
        f"",
        f"## r/{PRIMARY_SUB} — Top Posts",
        f"",
    ])

    if chicubs_posts:
        for i, post in enumerate(chicubs_posts[:20], 1):
            lines.append(format_post_markdown(post, i))
            lines.append("")
    else:
        lines.append("*No posts found.*")
        lines.append("")

    if baseball_posts:
        lines.extend([
            f"---",
            f"",
            f"## r/{SECONDARY_SUB} — Cubs Mentions",
            f"",
        ])
        for i, post in enumerate(baseball_posts[:10], 1):
            lines.append(format_post_markdown(post, i))
            lines.append("")

    lines.extend([
        f"---",
        f"",
        f"## Content Pipeline Notes",
        f"",
        f"Use the above to inform today's content mix:",
        f"",
        f"- **High-engagement threads** (50+ comments) = strong story candidates",
        f"- **Controversial posts** (low upvote ratio) = debate/hot-take material",
        f"- **Highly upvoted consensus** = lean into the shared fan energy",
        f"- **Recurring topics** = sustained interest worth covering",
        f"- **Game thread activity** = gauge excitement level for game-day content",
        f"",
    ])

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(
        description="Fetch Reddit fan sentiment for Cubs content pipeline"
    )
    parser.add_argument(
        "--sort", choices=["hot", "top", "new", "rising"], default="hot",
        help="Sort order (default: hot)"
    )
    parser.add_argument(
        "--time", choices=["hour", "day", "week", "month"], default="day",
        help="Time filter for 'top' sort (default: day)"
    )
    parser.add_argument(
        "--limit", type=int, default=25,
        help="Number of posts to fetch (default: 25, max: 100)"
    )
    parser.add_argument(
        "--include-rbaseball", action="store_true",
        help="Also scan r/baseball for Cubs mentions"
    )
    parser.add_argument(
        "--output", type=str, default=None,
        help="Output file path (default: reddit-sentiment-YYYY-MM-DD.md)"
    )
    parser.add_argument(
        "--content-folder", type=str, default=None,
        help="Place output in this content folder instead of current dir"
    )

    args = parser.parse_args()
    args.limit = min(args.limit, 100)

    today = datetime.now().strftime("%Y-%m-%d")

    print(f"🔍 Fetching r/{PRIMARY_SUB} ({args.sort})...")
    chicubs_posts = fetch_subreddit(PRIMARY_SUB, args.sort, args.time, args.limit)
    print(f"  ✓ Got {len(chicubs_posts)} posts from r/{PRIMARY_SUB}")

    baseball_posts = []
    if args.include_rbaseball:
        print(f"🔍 Fetching r/{SECONDARY_SUB} (filtering for Cubs)...")
        all_baseball = fetch_subreddit(SECONDARY_SUB, args.sort, args.time, 50)
        baseball_posts = filter_cubs_posts(all_baseball)
        print(f"  ✓ Got {len(baseball_posts)} Cubs-relevant posts from r/{SECONDARY_SUB}")

    # Calculate sentiment
    all_posts = chicubs_posts + baseball_posts
    sentiment = calculate_sentiment_signal(chicubs_posts)  # base sentiment on primary sub

    print(f"\n📊 Sentiment: {sentiment['mood']} | Energy: {sentiment['energy']}")
    print(f"   {sentiment['total_score']:,} upvotes across {sentiment['post_count']} posts")
    print(f"   {sentiment['total_comments']:,} total comments")

    # Generate output
    markdown = generate_markdown(chicubs_posts, baseball_posts, sentiment, args)

    # Determine output path
    if args.output:
        output_path = args.output
    elif args.content_folder:
        output_path = f"{args.content_folder}/reddit-sentiment-{today}.md"
    else:
        output_path = f"reddit-sentiment-{today}.md"

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(markdown)

    print(f"\n✓ Saved to: {output_path}")
    print(f"  Feed this into Step 1 research for fan sentiment context.")

    return 0


if __name__ == "__main__":
    sys.exit(main())
