#!/usr/bin/env python3
"""
Fetch Twitter/X Sentiment — Chicago Cubs Fan HQ

Pulls recent tweets about the Chicago Cubs using Twikit (unofficial Twitter API).
Requires a Twitter/X account for authentication (not an official API key).

FIRST-TIME SETUP:
    1. pip install twikit
    2. Create twitter-credentials.json in this directory:
       {
           "username": "your_twitter_username",
           "email": "your_email@example.com",
           "password": "your_password"
       }
    3. Run the script — it will log in and save cookies for future runs.

Usage:
    python fetch-twitter-sentiment.py                          # defaults: 40 tweets, "Top" sort
    python fetch-twitter-sentiment.py --sort Latest --limit 60
    python fetch-twitter-sentiment.py --queries "Cubs trade" "Wrigley Field"
    python fetch-twitter-sentiment.py --output custom-file.md

Output: twitter-sentiment-YYYY-MM-DD.md in the current directory (or dated content folder)

IMPORTANT: This uses an unofficial API. Twitter may change endpoints at any time.
           Use a burner account — there is a small risk of account suspension.
"""

import argparse
import asyncio
import io
import json
import os
import re
import sys
from datetime import datetime, timezone

# Fix Windows console encoding for emoji/unicode
if sys.platform == "win32":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8", errors="replace")

# Python 3.14+ compatibility: WindowsSelectorEventLoopPolicy is deprecated/removed.
# Twikit's __init__.py tries to set it on Windows. Patch asyncio before importing.
import warnings
with warnings.catch_warnings():
    warnings.simplefilter("ignore", DeprecationWarning)
    if sys.platform == "win32" and not hasattr(asyncio, "WindowsSelectorEventLoopPolicy"):
        asyncio.WindowsSelectorEventLoopPolicy = asyncio.DefaultEventLoopPolicy

try:
    from twikit import Client
except ImportError:
    print("ERROR: twikit is not installed.")
    print("  Run: pip install twikit")
    sys.exit(1)


# ─── Configuration ───────────────────────────────────────────────────────────

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
CREDENTIALS_FILE = os.path.join(SCRIPT_DIR, "twitter-credentials.json")
COOKIES_FILE = os.path.join(SCRIPT_DIR, ".twitter-cookies.json")

COOKIE_HELP_TEXT = """
MANUAL COOKIE EXPORT — Twitter/X

If Cloudflare blocks the login API, you can manually export cookies
from your browser and save them for this script.

Steps:
  1. Open Chrome and go to https://x.com (make sure you're logged in)
  2. Open DevTools (F12 or Ctrl+Shift+I)
  3. Go to the Application tab > Cookies > https://x.com
  4. Find these cookies and copy their values:
     - auth_token
     - ct0
  5. Create .twitter-cookies.json in this directory with:
     {
         "auth_token": "paste_auth_token_here",
         "ct0": "paste_ct0_here"
     }
  6. Run the script — it will use these cookies directly.

Alternative: Install browser_cookie3 to extract cookies automatically:
  pip install browser_cookie3
"""

# Default search queries — targeted for Chicago Cubs baseball content
DEFAULT_QUERIES = [
    "Chicago Cubs",
    "#Cubs MLB",
    "#GoCubs",
    "Cubs spring training",
]

# ─── Baseball Context Filter ────────────────────────────────────────────────
#
# Problem: "Cubs" matches animal cubs (bears, lions, wolves), Cub Scouts,
#          and other non-baseball topics.
#
# Solution: Two-layer filter.
#   1. BASEBALL_SIGNALS — if a tweet contains ANY of these, it's baseball. Keep it.
#   2. NON_BASEBALL_SIGNALS — if a tweet contains ANY of these AND zero baseball
#      signals, it's off-topic. Remove it.
#
# This is deliberately generous toward baseball content — we'd rather include
# a borderline tweet than miss a trending fan conversation.

BASEBALL_SIGNALS = [
    # Team & league context
    "mlb", "baseball", "nl central", "national league", "spring training",
    "opening day", "world series", "postseason", "playoffs", "all-star",
    "minor league", "aaa", "double-a", "triple-a",
    # Venue & broadcast
    "wrigley", "wrigleyville", "sloan park", "marquee sports", "marquee network",
    # Front office & org
    "jed hoyer", "carter hawkins", "tom ricketts", "ricketts family",
    "cubs farm", "cubs roster", "cubs bullpen", "cubs rotation",
    "cubs lineup", "cubs pitching", "cubs offense", "cubs defense",
    # Positions & game terms
    "pitcher", "pitching", "bullpen", "rotation", "lineup", "roster",
    "batting", "hitting", "home run", "strikeout", "era", "ops",
    "war ", "rbi", "obp", "slg", "whip", "innings",
    "trade", "free agent", "free agency", "signing", "contract",
    "draft", "prospect", "minors", "call-up", "callup", "dfa",
    "closer", "reliever", "starter", "designated hitter",
    # Division rivals (implies baseball context)
    "cardinals", "brewers", "reds", "pirates",
    "white sox", "crosstown",
    # Stadium/fan culture terms
    "ivy", "bleachers", "rooftop", "seventh inning", "fly the w",
    "cubbie", "cubbies", "northside", "north side",
    # Current roster names (2026 — update as needed)
    "bregman", "bellinger", "suzuki", "seiya", "happ",
    "hoerner", "swanson", "crow-armstrong", "pca",
    "imanaga", "steele", "horton", "taillon", "assad",
    "boyd", "rea", "cabrera", "brown",
    "ballesteros", "morel", "amaya", "caissie",
    "busch", "alcantara", "conforto", "mervis",
    "wicks", "little", "hodge", "mccormick",
    "counsell", "craig counsell",
]

NON_BASEBALL_SIGNALS = [
    # Animal cubs
    "bear cub", "lion cub", "wolf cub", "tiger cub", "fox cub",
    "baby bear", "baby lion", "baby animal", "zoo",
    "wildlife", "safari", "nature", "habitat", "den",
    "polar bear", "grizzly", "panda",
    # Cub Scouts / Boy Scouts
    "cub scout", "boy scout", "scouting", "eagle scout",
    "pack meeting", "den leader", "pinewood derby",
    # Other non-baseball "cubs"
    "cub cadet",  # lawn mower brand
    "mama bear",  # parenting context
    "cubs of the year",  # often animal awards
]


def is_baseball_tweet(text):
    """Determine if a tweet is about Chicago Cubs baseball.

    Returns:
        True if the tweet is likely about Cubs baseball.
        False if it's about animal cubs, Cub Scouts, etc.
    """
    lower = text.lower()

    # Check for explicit non-baseball signals first
    has_non_baseball = any(sig in lower for sig in NON_BASEBALL_SIGNALS)

    # Check for baseball signals
    has_baseball = any(sig in lower for sig in BASEBALL_SIGNALS)

    # If it has baseball signals, always keep it (even if it also mentions animals)
    if has_baseball:
        return True

    # If it has non-baseball signals and NO baseball signals, reject it
    if has_non_baseball:
        return False

    # Ambiguous — no strong signal either way.
    # Check if "cubs" appears near baseball-adjacent words via simple heuristics.
    # "Chicago Cubs" is already caught by DEFAULT_QUERIES, so most results
    # will have some baseball context. Keep ambiguous ones to avoid missing content.
    if "chicago" in lower:
        return True

    # Default: keep it. Most results from our targeted queries will be baseball.
    # The non-baseball filter catches the obvious false positives.
    return True


# ─── Twitter Client ──────────────────────────────────────────────────────────

def extract_cookies_from_browser():
    """Attempt to extract Twitter cookies from Chrome browser.

    Uses browser_cookie3 if installed. This bypasses Cloudflare blocks
    by reusing an existing browser session.
    """
    try:
        import browser_cookie3
    except ImportError:
        return None

    print("  Trying to extract cookies from Chrome...")
    try:
        cj = browser_cookie3.chrome(domain_name=".x.com")
        cookies = {}
        for cookie in cj:
            cookies[cookie.name] = cookie.value

        # Check for essential Twitter auth cookies
        essential = ["auth_token", "ct0"]
        if all(k in cookies for k in essential):
            print(f"  Found {len(cookies)} cookies from Chrome (auth_token + ct0 present)")
            return cookies
        else:
            print("  Chrome cookies found but missing auth_token/ct0 — not logged in?")
            return None
    except Exception as e:
        print(f"  Couldn't extract Chrome cookies: {e}")
        return None


async def create_client():
    """Create and authenticate a Twikit client.

    Auth priority:
      1. Saved twikit cookies (.twitter-cookies.json)
      2. Browser cookie extraction (if browser_cookie3 installed)
      3. Credential-based login (may be blocked by Cloudflare)
    """
    client = Client("en-US")

    # --- Priority 1: Saved twikit cookies ---
    if os.path.exists(COOKIES_FILE):
        try:
            client.load_cookies(COOKIES_FILE)
            print("  Loaded saved cookies")
            return client
        except Exception as e:
            print(f"  Couldn't load cookies ({e}), trying other methods...")

    # --- Priority 2: Browser cookie extraction ---
    browser_cookies = extract_cookies_from_browser()
    if browser_cookies:
        try:
            client.set_cookies(browser_cookies, clear_cookies=True)
            client.save_cookies(COOKIES_FILE)
            print("  Saved browser cookies for future runs")
            return client
        except Exception as e:
            print(f"  Browser cookies didn't work: {e}")

    # --- Priority 3: Credential login ---
    if not os.path.exists(CREDENTIALS_FILE):
        print(f"ERROR: No authentication method available.")
        print(f"\nOption A — Create {os.path.basename(CREDENTIALS_FILE)}:")
        print('  {')
        print('      "username": "your_twitter_username",')
        print('      "email": "your_email@example.com",')
        print('      "password": "your_password"')
        print('  }')
        print(f"\nOption B — Install browser_cookie3 to extract cookies from Chrome:")
        print('  pip install browser_cookie3')
        print('  (You must be logged into x.com in Chrome)')
        print(f"\nOption C — Manually export cookies (see --help-cookies flag)")
        sys.exit(1)

    with open(CREDENTIALS_FILE, "r", encoding="utf-8") as f:
        creds = json.load(f)

    print("  Logging in to Twitter/X...")
    try:
        await client.login(
            auth_info_1=creds["username"],
            auth_info_2=creds.get("email"),
            password=creds["password"],
            totp_secret=creds.get("totp_secret"),
        )
    except Exception as e:
        error_str = str(e)
        if "cloudflare" in error_str.lower() or "403" in error_str:
            print(f"\nBLOCKED BY CLOUDFLARE (403)")
            print(f"  Twitter/X is blocking this IP address via Cloudflare.")
            print(f"  This is common when running from cloud environments or VPNs.")
            print(f"\n  WORKAROUNDS:")
            print(f"  1. Run this script from your local terminal (PowerShell/CMD)")
            print(f"     Your residential IP is less likely to be blocked.")
            print(f"  2. Install browser_cookie3 to skip login entirely:")
            print(f"     pip install browser_cookie3")
            print(f"     (Extracts cookies from your Chrome browser session)")
            print(f"  3. Use --help-cookies for manual cookie export instructions.")
        else:
            print(f"ERROR: Login failed: {e}")
            print("  Check your credentials and try again.")
            print("  If using 2FA, add \"totp_secret\" to your credentials file.")
        sys.exit(1)

    # Save cookies for future runs
    client.save_cookies(COOKIES_FILE)
    print("  Logged in and saved cookies")

    return client


async def search_tweets(client, query, sort="Top", limit=20):
    """Search Twitter for tweets matching a query.

    Args:
        client: Authenticated Twikit client
        query: Search query string
        sort: "Top", "Latest", or "Media"
        limit: Max number of tweets to collect

    Returns:
        List of tweet dicts
    """
    tweets = []
    try:
        results = await client.search_tweet(query, product=sort, count=min(limit, 20))

        for tweet in results:
            tweets.append(extract_tweet_data(tweet))

        # Paginate if we need more
        pages_fetched = 1
        while len(tweets) < limit and results and pages_fetched < 5:
            try:
                await asyncio.sleep(2)  # Rate limit protection
                results = await results.next()
                if not results:
                    break
                for tweet in results:
                    tweets.append(extract_tweet_data(tweet))
                pages_fetched += 1
            except Exception:
                break  # Pagination ended or rate limited

    except Exception as e:
        print(f"  [warning] Search error for '{query}': {e}")

    return tweets[:limit]


def extract_tweet_data(tweet):
    """Extract relevant data from a Twikit Tweet object."""
    return {
        "id": tweet.id,
        "text": tweet.full_text or tweet.text or "",
        "likes": tweet.favorite_count or 0,
        "retweets": tweet.retweet_count or 0,
        "replies": tweet.reply_count or 0,
        "quotes": tweet.quote_count or 0,
        "views": tweet.view_count or 0,
        "created_at": tweet.created_at or "",
        "user_name": tweet.user.name if tweet.user else "",
        "user_handle": tweet.user.screen_name if tweet.user else "",
        "user_followers": tweet.user.followers_count if tweet.user else 0,
        "user_verified": tweet.user.is_blue_verified if tweet.user else False,
        "lang": tweet.lang or "",
        "is_retweet": tweet.retweeted_tweet is not None,
        "is_quote": tweet.quote is not None,
        "is_reply": tweet.in_reply_to is not None,
    }


# ─── Deduplication & Filtering ───────────────────────────────────────────────

def deduplicate_tweets(tweets):
    """Remove duplicate tweets (same tweet from multiple queries)."""
    seen_ids = set()
    unique = []
    for t in tweets:
        if t["id"] not in seen_ids:
            seen_ids.add(t["id"])
            unique.append(t)
    return unique


def filter_baseball_tweets(tweets):
    """Filter tweets to only Chicago Cubs baseball content.

    Removes tweets about animal cubs, Cub Scouts, and other off-topic results.
    """
    kept = []
    removed = 0
    for t in tweets:
        if is_baseball_tweet(t["text"]):
            kept.append(t)
        else:
            removed += 1

    if removed > 0:
        print(f"  [filter] Removed {removed} non-baseball tweet(s)")

    return kept


# ─── Sentiment Analysis ─────────────────────────────────────────────────────

def calculate_sentiment(tweets):
    """Calculate sentiment signals from tweet engagement patterns."""
    if not tweets:
        return {"mood": "unknown", "energy": "low", "tweet_count": 0}

    total_likes = sum(t["likes"] for t in tweets)
    total_retweets = sum(t["retweets"] for t in tweets)
    total_replies = sum(t["replies"] for t in tweets)
    total_views = sum(t["views"] for t in tweets)
    total_quotes = sum(t["quotes"] for t in tweets)

    # Engagement rate: (likes + retweets + replies) / views
    engagement_rate = 0
    if total_views > 0:
        engagement_rate = (total_likes + total_retweets + total_replies) / total_views

    # Energy based on total engagement
    total_engagement = total_likes + total_retweets + total_replies
    if total_engagement > len(tweets) * 100:
        energy = "high"
    elif total_engagement > len(tweets) * 20:
        energy = "moderate"
    else:
        energy = "low"

    # Mood: reply-heavy = debate, like-heavy = positive
    if total_replies > 0 and total_likes > 0:
        reply_ratio = total_replies / (total_likes + total_replies)
        if reply_ratio > 0.4:
            mood = "debating/divided"
        elif reply_ratio > 0.2:
            mood = "mixed/engaged"
        else:
            mood = "positive/united"
    else:
        mood = "positive/united"

    # Virality: any single tweet with outsized engagement?
    viral_tweets = [t for t in tweets if t["likes"] > 500 or t["retweets"] > 100]

    return {
        "mood": mood,
        "energy": energy,
        "tweet_count": len(tweets),
        "total_likes": total_likes,
        "total_retweets": total_retweets,
        "total_replies": total_replies,
        "total_views": total_views,
        "total_quotes": total_quotes,
        "engagement_rate": round(engagement_rate, 4),
        "viral_count": len(viral_tweets),
    }


# ─── Markdown Output ────────────────────────────────────────────────────────

def format_tweet_markdown(tweet, index):
    """Format a single tweet as markdown."""
    # Parse created_at if available
    age_str = ""
    if tweet["created_at"]:
        try:
            # Twikit returns format like "Wed Feb 25 14:30:00 +0000 2026"
            dt = datetime.strptime(tweet["created_at"], "%a %b %d %H:%M:%S %z %Y")
            age_hours = (datetime.now(timezone.utc) - dt).total_seconds() / 3600
            age_str = f"{age_hours:.0f}h ago" if age_hours < 48 else f"{age_hours/24:.0f}d ago"
        except (ValueError, TypeError):
            age_str = ""

    # Truncate tweet text for display
    text = tweet["text"].replace("\n", " ").strip()
    if len(text) > 280:
        text = text[:277] + "..."

    verified = " [check]" if tweet["user_verified"] else ""
    age_part = f" | {age_str}" if age_str else ""
    followers = f" ({tweet['user_followers']:,} followers)" if tweet["user_followers"] > 1000 else ""

    return (
        f"{index}. **@{tweet['user_handle']}**{verified}{followers}{age_part}\n"
        f"   > {text}\n"
        f"   [heart]{tweet['likes']:,} | "
        f"[retweet]{tweet['retweets']:,} | "
        f"[reply]{tweet['replies']:,} | "
        f"[views]{tweet['views']:,}"
    )


def generate_markdown(tweets, sentiment, queries, sort_mode):
    """Generate the full markdown output."""
    today = datetime.now().strftime("%Y-%m-%d")
    time_now = datetime.now().strftime("%I:%M %p CT")

    lines = [
        f"# Twitter/X Fan Sentiment -- {today}",
        f"",
        f"*Generated at {time_now} | "
        f"Queries: {', '.join(queries)} | "
        f"Sort: {sort_mode}*",
        f"",
        f"---",
        f"",
        f"## Sentiment Summary",
        f"",
        f"| Metric | Value |",
        f"|--------|-------|",
        f"| Overall Mood | **{sentiment['mood']}** |",
        f"| Fan Energy | **{sentiment['energy']}** |",
        f"| Tweets Analyzed | {sentiment['tweet_count']} |",
        f"| Total Likes | {sentiment['total_likes']:,} |",
        f"| Total Retweets | {sentiment['total_retweets']:,} |",
        f"| Total Replies | {sentiment['total_replies']:,} |",
        f"| Total Views | {sentiment['total_views']:,} |",
        f"| Engagement Rate | {sentiment['engagement_rate']:.2%} |",
        f"| Viral Tweets (500+ likes) | {sentiment['viral_count']} |",
        f"",
        f"---",
        f"",
    ]

    # Sort tweets by engagement (likes + retweets) for display
    sorted_tweets = sorted(
        tweets,
        key=lambda t: t["likes"] + t["retweets"],
        reverse=True,
    )

    # Top tweets section
    lines.extend([
        f"## Top Tweets by Engagement",
        f"",
    ])

    if sorted_tweets:
        for i, tweet in enumerate(sorted_tweets[:20], 1):
            lines.append(format_tweet_markdown(tweet, i))
            lines.append("")
    else:
        lines.append("*No tweets found.*")
        lines.append("")

    # Conversation starters (high reply count)
    reply_sorted = sorted(tweets, key=lambda t: t["replies"], reverse=True)
    reply_heavy = [t for t in reply_sorted if t["replies"] >= 5][:5]

    if reply_heavy:
        lines.extend([
            f"---",
            f"",
            f"## Hot Conversations (High Reply Count)",
            f"",
        ])
        for i, tweet in enumerate(reply_heavy, 1):
            lines.append(format_tweet_markdown(tweet, i))
            lines.append("")

    # Verified / high-follower accounts
    notable = [t for t in sorted_tweets if t["user_verified"] or t["user_followers"] > 10000][:5]

    if notable:
        lines.extend([
            f"---",
            f"",
            f"## Notable Accounts",
            f"",
        ])
        for i, tweet in enumerate(notable, 1):
            lines.append(format_tweet_markdown(tweet, i))
            lines.append("")

    # Pipeline notes
    lines.extend([
        f"---",
        f"",
        f"## Content Pipeline Notes",
        f"",
        f"Use the above to inform today's content mix:",
        f"",
        f"- **Viral tweets** (500+ likes) = trending topic, ride the wave",
        f"- **High-reply threads** = active debate, potential hot-take material",
        f"- **Verified/notable accounts** = amplify or respond for engagement",
        f"- **Common themes** = sustained fan interest worth covering",
        f"- **Engagement rate** = overall Cubs Twitter activity level",
        f"",
    ])

    return "\n".join(lines)


# ─── Main ────────────────────────────────────────────────────────────────────

async def async_main(args):
    """Async main — handles Twitter client and search."""

    queries = args.queries or DEFAULT_QUERIES

    print(f"Authenticating with Twitter/X...")
    client = await create_client()

    all_tweets = []

    for query in queries:
        print(f"Searching: '{query}' ({args.sort})...")
        tweets = await search_tweets(client, query, sort=args.sort, limit=args.limit)
        print(f"  Got {len(tweets)} tweets")
        all_tweets.extend(tweets)
        await asyncio.sleep(3)  # Delay between queries to avoid rate limits

    # Deduplicate (same tweet may appear in multiple queries)
    print(f"\nProcessing {len(all_tweets)} total tweets...")
    all_tweets = deduplicate_tweets(all_tweets)
    print(f"  {len(all_tweets)} unique tweets after dedup")

    # Filter to baseball-only content
    all_tweets = filter_baseball_tweets(all_tweets)
    print(f"  {len(all_tweets)} tweets after baseball filter")

    # Remove pure retweets (they duplicate content)
    original_tweets = [t for t in all_tweets if not t["is_retweet"]]
    print(f"  {len(original_tweets)} original tweets (retweets removed)")

    # Calculate sentiment
    sentiment = calculate_sentiment(original_tweets)

    print(f"\nSentiment: {sentiment['mood']} | Energy: {sentiment['energy']}")
    print(f"   {sentiment['total_likes']:,} likes | {sentiment['total_retweets']:,} RTs | {sentiment['total_replies']:,} replies")
    if sentiment["total_views"] > 0:
        print(f"   {sentiment['total_views']:,} views | {sentiment['engagement_rate']:.2%} engagement")

    # Generate markdown
    markdown = generate_markdown(original_tweets, sentiment, queries, args.sort)

    # Determine output path
    today = datetime.now().strftime("%Y-%m-%d")
    if args.output:
        output_path = args.output
    elif args.content_folder:
        output_path = f"{args.content_folder}/twitter-sentiment-{today}.md"
    else:
        output_path = f"twitter-sentiment-{today}.md"

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(markdown)

    print(f"\nSaved to: {output_path}")
    print(f"  Feed this into Step 1 research for fan sentiment context.")

    # Save cookies after successful run
    try:
        client.save_cookies(COOKIES_FILE)
    except Exception:
        pass

    return 0


def main():
    parser = argparse.ArgumentParser(
        description="Fetch Twitter/X fan sentiment for Cubs content pipeline"
    )
    parser.add_argument(
        "--sort", choices=["Top", "Latest", "Media"], default="Top",
        help="Sort mode (default: Top)"
    )
    parser.add_argument(
        "--limit", type=int, default=20,
        help="Tweets per query (default: 20). Total = limit x number of queries."
    )
    parser.add_argument(
        "--queries", nargs="+", type=str, default=None,
        help="Custom search queries (default: Chicago Cubs, #Cubs MLB, #GoCubs, Cubs spring training)"
    )
    parser.add_argument(
        "--output", type=str, default=None,
        help="Output file path (default: twitter-sentiment-YYYY-MM-DD.md)"
    )
    parser.add_argument(
        "--content-folder", type=str, default=None,
        help="Place output in this content folder instead of current dir"
    )
    parser.add_argument(
        "--help-cookies", action="store_true",
        help="Show instructions for manually exporting browser cookies"
    )

    args = parser.parse_args()

    if args.help_cookies:
        print(COOKIE_HELP_TEXT)
        return 0

    return asyncio.run(async_main(args))


if __name__ == "__main__":
    sys.exit(main())
