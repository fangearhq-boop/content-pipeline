#!/usr/bin/env python3
"""
Write content pipeline stats to Supabase after each pipeline run.

Usage:
    python write-pipeline-stats.py --niche Softball 2026-03-20

Reads the 07-content-data.json from the content folder and writes
a summary row to the content_pipeline_daily table.
"""

import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path

# Fix Unicode on Windows
if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')

try:
    import psycopg2
except ImportError:
    print("ERROR: psycopg2 not installed. Run: pip install psycopg2-binary")
    sys.exit(1)


# Supabase connection
SUPABASE_DB_HOST = os.environ.get("FANHQ_DB_HOST", "aws-0-us-west-2.pooler.supabase.com")
SUPABASE_DB_PORT = int(os.environ.get("FANHQ_DB_PORT", "6543"))
SUPABASE_DB_NAME = os.environ.get("FANHQ_DB_NAME", "postgres")
SUPABASE_DB_USER = os.environ.get("FANHQ_DB_USER", "postgres.pxlcvqhfpspjjsvldtno")
SUPABASE_DB_PASS = os.environ.get("FANHQ_DB_PASS", "U3B4CmFDBGxYJcvE")


def get_db_connection():
    return psycopg2.connect(
        host=SUPABASE_DB_HOST,
        port=SUPABASE_DB_PORT,
        dbname=SUPABASE_DB_NAME,
        user=SUPABASE_DB_USER,
        password=SUPABASE_DB_PASS,
        sslmode='require'
    )


def load_niche_config(niche_folder):
    config_path = niche_folder / "niche-config.yaml"
    if not config_path.exists():
        return {}
    config = {}
    with open(config_path, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if ':' in line and not line.startswith('#') and not line.startswith('-'):
                key, _, value = line.partition(':')
                key = key.strip()
                value = value.strip().strip('"').strip("'")
                if value:
                    config[key] = value
    return config


def main():
    args = sys.argv[1:]
    niche_name = None
    date_str = None

    i = 0
    while i < len(args):
        if args[i] == '--niche' and i + 1 < len(args):
            niche_name = args[i + 1]
            i += 2
        elif not date_str and not args[i].startswith('-'):
            date_str = args[i]
            i += 1
        else:
            i += 1

    if not niche_name:
        print("Usage: python write-pipeline-stats.py --niche <NicheName> [YYYY-MM-DD]")
        sys.exit(1)

    if not date_str:
        date_str = datetime.now(timezone.utc).strftime("%Y-%m-%d")

    # Script is at Niche_Launches/_engine/scripts/X.py
    # .parent = scripts/, .parent.parent = _engine/, .parent.parent.parent = Niche_Launches/
    niche_launches = Path(__file__).resolve().parent.parent.parent
    niche_folder = niche_launches / niche_name

    if not niche_folder.exists():
        # Case-insensitive search
        for entry in niche_launches.iterdir():
            if entry.is_dir() and entry.name.lower() == niche_name.lower():
                niche_folder = entry
                break

    config = load_niche_config(niche_folder)
    content_prefix = config.get("content_prefix", f"{niche_name.lower()}-content")
    brand_name = config.get("brand_name", niche_name)
    brand_short = config.get("brand_short", niche_name).lower()

    # Load content data JSON
    content_folder = niche_folder / f"{content_prefix}-{date_str}"
    json_path = content_folder / "07-content-data.json"

    if not json_path.exists():
        print(f"No content data found at {json_path}")
        sys.exit(1)

    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    stats = data.get("pipeline_stats", {})
    stories = data.get("stories", [])

    # Count tiers
    tier1 = sum(1 for s in stories if s.get("tier") == 1 or s.get("tier") == "1")
    tier2 = sum(1 for s in stories if s.get("tier") == 2 or s.get("tier") == "2")
    tier3 = sum(1 for s in stories if s.get("tier") == 3 or s.get("tier") == "3")

    # Dashboard URL
    dashboard_url = f"https://fangearhq-boop.github.io/content-dashboards/{brand_short}/{date_str}.html"

    # Write to Supabase
    conn = get_db_connection()
    conn.autocommit = True
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO content_pipeline_daily
            (date, niche, brand_name, stories_count, x_posts_count, tobi_posts_count,
             articles_count, tier1_count, tier2_count, tier3_count, dashboard_url)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        ON CONFLICT (date, niche) DO UPDATE SET
            stories_count = EXCLUDED.stories_count,
            x_posts_count = EXCLUDED.x_posts_count,
            tobi_posts_count = EXCLUDED.tobi_posts_count,
            articles_count = EXCLUDED.articles_count,
            tier1_count = EXCLUDED.tier1_count,
            tier2_count = EXCLUDED.tier2_count,
            tier3_count = EXCLUDED.tier3_count,
            dashboard_url = EXCLUDED.dashboard_url
    """, (
        date_str, brand_short, brand_name,
        stats.get("total_stories", 0),
        stats.get("x_posts_count", 0),
        stats.get("x_posts_count", 0),  # TOBI = same count as X posts
        stats.get("articles_count", 0),
        tier1, tier2, tier3,
        dashboard_url,
    ))

    print(f"Written: {brand_name} ({brand_short}) {date_str}")
    print(f"  Stories: {stats.get('total_stories', 0)} | X: {stats.get('x_posts_count', 0)} | Articles: {stats.get('articles_count', 0)}")

    cur.close()
    conn.close()


if __name__ == "__main__":
    main()
