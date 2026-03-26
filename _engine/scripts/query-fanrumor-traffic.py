#!/usr/bin/env python3
"""
Query GA4 traffic data for fanrumor.com and filter to softball content.

Outputs a JSON file that the review dashboard can consume to display
content performance metrics.

Usage:
    python query-fanrumor-traffic.py --niche Softball --output traffic-data.json
    python query-fanrumor-traffic.py --niche Softball --days 30

Requires:
    - GA4_SERVICE_ACCOUNT_JSON env var (base64-encoded service account)
    - google-analytics-data Python package
"""

import os
import sys
import json
import argparse
import logging
from datetime import datetime, timedelta
from pathlib import Path

logging.basicConfig(level="INFO", format="%(asctime)s [%(name)s] %(levelname)s: %(message)s")
log = logging.getLogger("fanrumor-traffic")

# GA4 property ID for fanrumor.com
FANRUMOR_PROPERTY_ID = "377089089"

# Keywords that identify softball content in page titles
SOFTBALL_KEYWORDS = [
    "softball", "strikeout", "no-hitter", "perfect game", "pitcher's circle",
    "home run", "run-rule", "ncaa", "nfca", "wcws",
    # Player/team names from the pipeline
    "wells", "pickens", "kavan", "briski", "rothrock", "canady", "mardjetko",
    "tennessee", "alabama", "texas tech", "oklahoma", "florida", "gcu",
    "grand canyon", "ole miss", "arkansas", "lsu", "baylor",
    "big 12", "sec ", " acc ", "mountain west",
    "torres", "jensen", "hasler", "stewart", "leach",
]


GA4_KEY_FILE = os.path.join(os.path.expanduser("~"), ".claude", "keys", "ga4-service-account.b64")


def get_ga4_client():
    """Initialize GA4 Data API client from service account."""
    import os
    sa_json = os.environ.get("GA4_SERVICE_ACCOUNT_JSON", "")
    if not sa_json and os.path.isfile(GA4_KEY_FILE):
        with open(GA4_KEY_FILE, "r") as f:
            sa_json = f.read().strip()
        log.info("Loaded GA4 key from %s", GA4_KEY_FILE)
    if not sa_json:
        log.error("GA4_SERVICE_ACCOUNT_JSON not set and %s not found", GA4_KEY_FILE)
        return None

    try:
        from google.analytics.data_v1beta import BetaAnalyticsDataClient
        from google.oauth2 import service_account
        import base64

        creds_json = json.loads(base64.b64decode(sa_json))
        credentials = service_account.Credentials.from_service_account_info(creds_json)
        return BetaAnalyticsDataClient(credentials=credentials)
    except ImportError:
        log.error("google-analytics-data not installed. Run: pip install google-analytics-data")
        return None
    except Exception as e:
        log.error("Failed to init GA4 client: %s", e)
        return None


def is_softball_page(path, title):
    """Check if a page is softball content based on path and title."""
    combined = (path + " " + title).lower()
    return any(kw in combined for kw in SOFTBALL_KEYWORDS)


def query_traffic_summary(client, start_date, end_date):
    """Get daily traffic totals for fanrumor.com."""
    from google.analytics.data_v1beta import RunReportRequest, DateRange, Dimension, Metric

    request = RunReportRequest(
        property=f"properties/{FANRUMOR_PROPERTY_ID}",
        date_ranges=[DateRange(start_date=start_date, end_date=end_date)],
        dimensions=[Dimension(name="date")],
        metrics=[
            Metric(name="sessions"),
            Metric(name="screenPageViews"),
            Metric(name="activeUsers"),
            Metric(name="bounceRate"),
        ],
    )
    response = client.run_report(request)

    daily = []
    for row in response.rows:
        date_raw = row.dimension_values[0].value
        daily.append({
            "date": f"{date_raw[:4]}-{date_raw[4:6]}-{date_raw[6:8]}",
            "sessions": int(row.metric_values[0].value),
            "pageviews": int(row.metric_values[1].value),
            "users": int(row.metric_values[2].value),
            "bounce_rate": round(float(row.metric_values[3].value), 3),
        })

    daily.sort(key=lambda x: x["date"])
    return daily


def query_top_pages(client, start_date, end_date, limit=50):
    """Get top pages by pageviews, filtered to softball content."""
    from google.analytics.data_v1beta import RunReportRequest, DateRange, Dimension, Metric

    request = RunReportRequest(
        property=f"properties/{FANRUMOR_PROPERTY_ID}",
        date_ranges=[DateRange(start_date=start_date, end_date=end_date)],
        dimensions=[Dimension(name="pagePath"), Dimension(name="pageTitle")],
        metrics=[
            Metric(name="screenPageViews"),
            Metric(name="activeUsers"),
            Metric(name="averageSessionDuration"),
        ],
        limit=200,  # Fetch more, then filter
    )
    response = client.run_report(request)

    pages = []
    for row in response.rows:
        path = row.dimension_values[0].value
        title = row.dimension_values[1].value
        pv = int(row.metric_values[0].value)
        users = int(row.metric_values[1].value)
        avg_dur = round(float(row.metric_values[2].value), 1)

        if is_softball_page(path, title) and path != "/":
            pages.append({
                "path": path,
                "title": title,
                "pageviews": pv,
                "users": users,
                "avg_duration_sec": avg_dur,
            })

    pages.sort(key=lambda x: x["pageviews"], reverse=True)
    return pages[:limit]


def query_softball_monthly(client, months=6):
    """Get monthly softball pageviews for the last N months."""
    from google.analytics.data_v1beta import RunReportRequest, DateRange, Dimension, Metric

    now = datetime.now()
    # Go back N full months + current partial month
    start = datetime(now.year, now.month, 1)
    for _ in range(months):
        start = (start - timedelta(days=1)).replace(day=1)
    start_date = start.strftime("%Y-%m-%d")
    end_date = now.strftime("%Y-%m-%d")

    request = RunReportRequest(
        property=f"properties/{FANRUMOR_PROPERTY_ID}",
        date_ranges=[DateRange(start_date=start_date, end_date=end_date)],
        dimensions=[
            Dimension(name="yearMonth"),
            Dimension(name="pagePath"),
            Dimension(name="pageTitle"),
        ],
        metrics=[
            Metric(name="screenPageViews"),
            Metric(name="activeUsers"),
        ],
        limit=10000,
    )
    response = client.run_report(request)

    # Aggregate softball pages by month
    monthly = {}
    for row in response.rows:
        ym = row.dimension_values[0].value  # "202603"
        path = row.dimension_values[1].value
        title = row.dimension_values[2].value
        pv = int(row.metric_values[0].value)
        users = int(row.metric_values[1].value)

        if not is_softball_page(path, title) or path == "/":
            continue

        if ym not in monthly:
            monthly[ym] = {"yearMonth": ym, "pageviews": 0, "users": 0, "articles": 0}
        monthly[ym]["pageviews"] += pv
        monthly[ym]["users"] += users
        monthly[ym]["articles"] += 1

    result = sorted(monthly.values(), key=lambda x: x["yearMonth"])

    # Format yearMonth for display (e.g. "202603" -> "Mar 2026")
    import calendar
    for entry in result:
        ym = entry["yearMonth"]
        y, m = int(ym[:4]), int(ym[4:6])
        entry["label"] = f"{calendar.month_abbr[m]} {y}"

    return result


def query_traffic_sources(client, start_date, end_date):
    """Get traffic sources for fanrumor.com."""
    from google.analytics.data_v1beta import RunReportRequest, DateRange, Dimension, Metric

    request = RunReportRequest(
        property=f"properties/{FANRUMOR_PROPERTY_ID}",
        date_ranges=[DateRange(start_date=start_date, end_date=end_date)],
        dimensions=[Dimension(name="sessionSource"), Dimension(name="sessionMedium")],
        metrics=[
            Metric(name="sessions"),
            Metric(name="screenPageViews"),
            Metric(name="activeUsers"),
        ],
        limit=20,
    )
    response = client.run_report(request)

    sources = []
    for row in response.rows:
        sources.append({
            "source": row.dimension_values[0].value,
            "medium": row.dimension_values[1].value,
            "sessions": int(row.metric_values[0].value),
            "pageviews": int(row.metric_values[1].value),
            "users": int(row.metric_values[2].value),
        })

    sources.sort(key=lambda x: x["sessions"], reverse=True)
    return sources


def main():
    parser = argparse.ArgumentParser(description="Query fanrumor.com GA4 traffic for softball content")
    parser.add_argument("--niche", type=str, default="Softball", help="Niche name (for output path)")
    parser.add_argument("--output", type=str, help="Output JSON file path (default: auto in content folder)")
    parser.add_argument("--days", type=int, default=30, help="Days of history to query (default 30)")
    args = parser.parse_args()

    client = get_ga4_client()
    if not client:
        log.error("Cannot connect to GA4. Skipping traffic data.")
        sys.exit(1)

    now = datetime.now()
    end_date = now.strftime("%Y-%m-%d")

    # 7-day window
    start_7d = (now - timedelta(days=7)).strftime("%Y-%m-%d")
    # 30-day window
    start_30d = (now - timedelta(days=30)).strftime("%Y-%m-%d")
    # Previous 7 days for comparison
    prev_start_7d = (now - timedelta(days=14)).strftime("%Y-%m-%d")
    prev_end_7d = (now - timedelta(days=7)).strftime("%Y-%m-%d")

    log.info("Querying fanrumor.com GA4 (property %s)", FANRUMOR_PROPERTY_ID)

    # 1. Daily traffic (last 30 days for the chart)
    log.info("Fetching daily traffic (last 30 days)...")
    daily_30d = query_traffic_summary(client, start_30d, end_date)

    # Compute 7-day and 30-day totals
    seven_day_cutoff = start_7d
    daily_7d = [d for d in daily_30d if d["date"] >= seven_day_cutoff]
    totals_7d = {
        "sessions": sum(d["sessions"] for d in daily_7d),
        "pageviews": sum(d["pageviews"] for d in daily_7d),
        "users": sum(d["users"] for d in daily_7d),
    }
    totals_30d = {
        "sessions": sum(d["sessions"] for d in daily_30d),
        "pageviews": sum(d["pageviews"] for d in daily_30d),
        "users": sum(d["users"] for d in daily_30d),
    }

    # 2. Previous 7 days for week-over-week comparison
    log.info("Fetching previous 7 days for comparison...")
    daily_prev = query_traffic_summary(client, prev_start_7d, prev_end_7d)
    totals_prev_7d = {
        "sessions": sum(d["sessions"] for d in daily_prev),
        "pageviews": sum(d["pageviews"] for d in daily_prev),
        "users": sum(d["users"] for d in daily_prev),
    }

    # 3. Top softball pages (7-day and 30-day)
    log.info("Fetching top softball pages (7-day)...")
    top_pages_7d = query_top_pages(client, start_7d, end_date, limit=20)
    log.info("Fetching top softball pages (30-day)...")
    top_pages_30d = query_top_pages(client, start_30d, end_date, limit=30)

    # Sum softball-only pageviews
    softball_pv_7d = sum(p["pageviews"] for p in top_pages_7d)
    softball_pv_30d = sum(p["pageviews"] for p in top_pages_30d)

    # 4. Traffic sources (7-day)
    log.info("Fetching traffic sources (7-day)...")
    sources_7d = query_traffic_sources(client, start_7d, end_date)

    # 5. Monthly softball pageviews (last 6 months)
    log.info("Fetching monthly softball pageviews (6 months)...")
    monthly_softball = query_softball_monthly(client, months=6)

    # Build output
    result = {
        "generated_at": now.isoformat(),
        "property": "fanrumor.com",
        "property_id": FANRUMOR_PROPERTY_ID,
        "summary": {
            "7d": totals_7d,
            "30d": totals_30d,
            "prev_7d": totals_prev_7d,
            "softball_pageviews_7d": softball_pv_7d,
            "softball_pageviews_30d": softball_pv_30d,
        },
        "daily": daily_30d,
        "top_pages_7d": top_pages_7d,
        "top_pages_30d": top_pages_30d,
        "sources_7d": sources_7d,
        "monthly_softball": monthly_softball,
    }

    # Determine output path
    if args.output:
        output_path = Path(args.output)
    else:
        # Default: put in the niche's root folder
        niche_root = Path(__file__).resolve().parent.parent.parent / args.niche
        output_path = niche_root / "fanrumor-traffic.json"

    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(result, f, indent=2)

    log.info("Traffic data written to %s", output_path)
    log.info("Site totals (7d): %s sessions, %s pv, %s users",
             f"{totals_7d['sessions']:,}", f"{totals_7d['pageviews']:,}", f"{totals_7d['users']:,}")
    log.info("Softball pages (7d): %s pv across %d articles",
             f"{softball_pv_7d:,}", len(top_pages_7d))
    log.info("Softball pages (30d): %s pv across %d articles",
             f"{softball_pv_30d:,}", len(top_pages_30d))


if __name__ == "__main__":
    main()
