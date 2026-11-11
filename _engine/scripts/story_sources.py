"""Structured per-story source harvesting for 07-content-data.json.

Produces ``stories[].sources[]`` entries of the shape::

    {"name": "U.S. Consumer Product Safety Commission",
     "url": "https://www.cpsc.gov/Recalls/...",
     "official": true,
     "found_in": ["01-research-notes.md"]}

Downstream consumers (springs-daily parenting ingest) read ``name``, ``url``
and ``official``; extra fields such as ``title``, ``publisher`` and
``found_in`` are ignored by them.

Hard rule: URLs are ONLY ever copied from text the pipeline already wrote
(research notes, fact-check log, daily brief, article HTML). Nothing here
builds, guesses, or "upgrades" a URL. A bare domain mention like
"CPSC.gov recall listing" with no http(s):// URL produces no source.
"""

import os
import re
from urllib.parse import urlsplit, urlunsplit

# Hosts treated as official. Matches the list springs-daily PR #338 uses.
OFFICIAL_SUFFIXES = ('.gov', '.mil', '.edu', '.us')
OFFICIAL_HOSTS = frozenset({
    # Pikes Peak region school districts
    'd11.org', 'asd20.org', 'd49.org', 'hsd2.org', 'wsd3.org', 'ffc8.org',
    'lewispalmer.org', 'cmsd12.org', 'mssd14.org',
    # County / utilities / library
    'elpasoco.com', 'elpasocountyhealth.org', 'csu.org', 'ppld.org',
    # Health authorities
    'aap.org', 'healthychildren.org', 'who.int',
})

# Display names for official hosts, used only when the material gives no
# better label (e.g. an <a> whose anchor text is just "cpsc.gov").
OFFICIAL_PUBLISHER_NAMES = {
    'cpsc.gov': 'U.S. Consumer Product Safety Commission',
    'cdc.gov': 'Centers for Disease Control and Prevention',
    'fda.gov': 'U.S. Food and Drug Administration',
    'nhtsa.gov': 'National Highway Traffic Safety Administration',
    'aap.org': 'American Academy of Pediatrics',
    'healthychildren.org': 'American Academy of Pediatrics (HealthyChildren.org)',
    'who.int': 'World Health Organization',
    'd11.org': 'Colorado Springs School District 11',
    'asd20.org': 'Academy District 20',
    'd49.org': 'School District 49',
    'elpasoco.com': 'El Paso County',
    'elpasocountyhealth.org': 'El Paso County Public Health',
    'ppld.org': 'Pikes Peak Library District',
    'csu.org': 'Colorado Springs Utilities',
    'coloradosprings.gov': 'City of Colorado Springs',
}

# Marker an author can put on a source line to vouch that a non-listed host
# (an organizer's or private school's own page) is the official source.
OFFICIAL_MARKER_RE = re.compile(r'\[\s*OFFICIAL\s*\]', re.IGNORECASE)

DEFAULT_MAX_SOURCES = 8

# Story headers seen in Parenting notes: "## Story 1:", "### STORY 1:",
# "### Story 1 —", "## STORY 1:". Story ids like "2A" map to story 2.
STORY_HEADER_RE = re.compile(r'^#{2,4}\s*STORY\s+(\d+)[A-Za-z]?\b.*$',
                             re.IGNORECASE | re.MULTILINE)

_URL_RE = re.compile(r'https?://[^\s<>"\'`\]\[)(|]+', re.IGNORECASE)
_HREF_RE = re.compile(r'<a\b[^>]*?href\s*=\s*["\'](https?://[^"\']+)["\'][^>]*>(.*?)</a>',
                      re.IGNORECASE | re.DOTALL)
_MD_LINK_RE = re.compile(r'\[([^\]]+)\]\((https?://[^)\s]+)\)', re.IGNORECASE)
_TRAILING_PUNCT = '.,;:!?\'"*_'


# ---------------------------------------------------------------------------
# Host / URL helpers
# ---------------------------------------------------------------------------

def host_of(url):
    try:
        host = (urlsplit(url).hostname or '').lower()
    except ValueError:
        return ''
    return host[4:] if host.startswith('www.') else host


def _host_matches(host, domain):
    return host == domain or host.endswith('.' + domain)


def is_official_host(url):
    host = host_of(url)
    if not host:
        return False
    if host.endswith(OFFICIAL_SUFFIXES):
        return True
    return any(_host_matches(host, d) for d in OFFICIAL_HOSTS)


def clean_url(raw):
    """Trim trailing punctuation that prose/markdown glues onto a URL.

    Only removes characters around the URL; never adds or rewrites path parts.
    Returns '' when the result is not a usable http(s) URL.
    """
    url = (raw or '').strip()
    while url and url[-1] in _TRAILING_PUNCT:
        url = url[:-1]
    if not re.match(r'^https?://', url, re.IGNORECASE):
        return ''
    try:
        parts = urlsplit(url)
    except ValueError:
        return ''
    if not parts.hostname or '.' not in parts.hostname:
        return ''
    return url


def dedupe_key(url):
    """Key for de-duplication: case-insensitive scheme/host, no fragment,
    no trailing slash, http/https and www. treated as the same page."""
    parts = urlsplit(url)
    path = parts.path.rstrip('/')
    return urlunsplit(('', host_of(url), path, parts.query, ''))


def parse_host_list(value):
    """Parse a comma/space separated host list from niche-config."""
    if not value:
        return set()
    if isinstance(value, (list, tuple, set)):
        items = value
    else:
        items = re.split(r'[,\s]+', str(value))
    out = set()
    for item in items:
        item = item.strip().strip('"\'').lower()
        if not item:
            continue
        if '://' in item:
            item = host_of(item)
        elif item.startswith('www.'):
            item = item[4:]
        if item:
            out.add(item.split('/')[0])
    return out


# ---------------------------------------------------------------------------
# Story splitting
# ---------------------------------------------------------------------------

def split_by_story(content):
    """Return {story_num: section_text} for any supported header style."""
    result = {}
    if not content:
        return result
    headers = list(STORY_HEADER_RE.finditer(content))
    for i, m in enumerate(headers):
        num = int(m.group(1))
        start = m.start()
        end = headers[i + 1].start() if i + 1 < len(headers) else len(content)
        section = content[start:end]
        # Stop at the next same-or-higher level non-story heading
        # (e.g. "## Publishing Schedule" after the last story).
        level = len(m.group(0)) - len(m.group(0).lstrip('#'))
        tail = re.search(r'^#{1,%d}\s+(?!STORY\b)\S' % level, section[len(m.group(0)):],
                         re.IGNORECASE | re.MULTILINE)
        if tail:
            section = section[:len(m.group(0)) + tail.start()]
        result[num] = result.get(num, '') + section
    return result


# ---------------------------------------------------------------------------
# Name extraction
# ---------------------------------------------------------------------------

def _strip_md(text):
    text = re.sub(r'<[^>]+>', ' ', text)
    text = re.sub(r'[*_`]+', '', text)
    text = OFFICIAL_MARKER_RE.sub('', text)
    text = re.sub(r'\s+', ' ', text)
    return text.strip()


def _default_name(url):
    host = host_of(url)
    for domain, name in OFFICIAL_PUBLISHER_NAMES.items():
        if _host_matches(host, domain):
            return name
    return host


def _looks_like_domain(text):
    return bool(re.fullmatch(r'(?:https?://)?(?:www\.)?[\w.-]+\.[a-z]{2,}(?:/\S*)?', text.strip(),
                             re.IGNORECASE))


def _name_from_line(line, url_start):
    """Derive title/publisher from the text before a URL on one line.

    Handles shapes seen in research notes:
      - D49: "District 49 Launches ..." — https://...
      - CPSC.gov recall listing: https://...
      - CPR News Jan 2026 (context): https://...
    Returns (name, title, publisher), any of which may be ''.
    """
    before = line[:url_start]
    before = re.sub(r'^\s*(?:[-*+]|\d+[.)])\s+', '', before)
    before = re.sub(r'^\s*(?:URL|Link|Source)s?\s*:\s*$', '', before, flags=re.IGNORECASE)
    before = _strip_md(before)
    before = re.sub(r'[\s—–:\-|(]+$', '', before).strip()
    title = ''
    publisher = ''
    q = re.search(r'["“]([^"”]{3,})["”]', before)
    if q:
        title = q.group(1).strip()
        pub = before[:q.start()]
        publisher = re.sub(r'[\s—–:\-|]+$', '', pub).strip()
    elif ':' in before:
        publisher, _, rest = before.partition(':')
        publisher = publisher.strip()
        title = rest.strip()
    else:
        publisher = before
    if publisher.lower() in ('url', 'link', 'source', 'sources'):
        publisher = ''
    name = title or publisher
    if name and _looks_like_domain(name):
        name = ''
    return name, title, publisher


# ---------------------------------------------------------------------------
# Extraction
# ---------------------------------------------------------------------------

def extract_sources_from_markdown(text, origin):
    """Every http(s) URL literally present in markdown text, with a label."""
    found = []
    if not text:
        return found
    for line in text.splitlines():
        vouched = bool(OFFICIAL_MARKER_RE.search(line))
        md_spans = []
        for m in _MD_LINK_RE.finditer(line):
            url = clean_url(m.group(2))
            md_spans.append((m.start(), m.end()))
            if url:
                label = _strip_md(m.group(1))
                found.append(_make(url, '' if _looks_like_domain(label) else label,
                                   label, '', origin, vouched))
        for m in _URL_RE.finditer(line):
            if any(s <= m.start() < e for s, e in md_spans):
                continue
            url = clean_url(m.group(0))
            if not url:
                continue
            name, title, publisher = _name_from_line(line, m.start())
            found.append(_make(url, name, title, publisher, origin, vouched))
    return found


def extract_sources_from_html(html, origin):
    """URLs from <a href> anchors (with anchor text), then bare URLs in text."""
    found = []
    if not html:
        return found
    seen = set()
    for m in _HREF_RE.finditer(html):
        url = clean_url(m.group(1))
        if not url:
            continue
        label = _strip_md(m.group(2))
        name = '' if (not label or _looks_like_domain(label)) else label
        found.append(_make(url, name, label if name else '', '', origin, False))
        seen.add(url)
    text_only = re.sub(r'<a\b[^>]*>.*?</a>', ' ', html, flags=re.IGNORECASE | re.DOTALL)
    text_only = re.sub(r'<[^>]+>', ' ', text_only)
    for m in _URL_RE.finditer(text_only):
        url = clean_url(m.group(0))
        if url and url not in seen:
            found.append(_make(url, '', '', '', origin, False))
            seen.add(url)
    return found


def _make(url, name, title, publisher, origin, vouched):
    entry = {
        'name': name or _default_name(url),
        'url': url,
        'official': bool(vouched or is_official_host(url)),
        'found_in': [origin],
    }
    if title and title != entry['name']:
        entry['title'] = title
    if publisher and publisher != entry['name']:
        entry['publisher'] = publisher
    return entry


def rank_and_cap(candidates, exclude_hosts=None, max_sources=DEFAULT_MAX_SOURCES):
    """Drop excluded hosts, dedupe by URL, official first, cap the list.

    Order within each group (official / other) follows first appearance, so
    research-note sources come before fact-check and article links.
    """
    exclude_hosts = exclude_hosts or set()
    merged = {}
    order = []
    for c in candidates:
        host = host_of(c['url'])
        if any(_host_matches(host, ex) for ex in exclude_hosts):
            continue
        key = dedupe_key(c['url'])
        if key in merged:
            m = merged[key]
            m['official'] = m['official'] or c['official']
            for origin in c.get('found_in', []):
                if origin not in m['found_in']:
                    m['found_in'].append(origin)
            # Prefer a real label over a host-derived default
            if m['name'] in (host, _default_name(m['url'])) and c['name'] not in (host, _default_name(c['url'])):
                m['name'] = c['name']
            continue
        merged[key] = {k: (list(v) if isinstance(v, list) else v) for k, v in c.items()}
        order.append(key)
    ranked = ([merged[k] for k in order if merged[k]['official']] +
              [merged[k] for k in order if not merged[k]['official']])
    return ranked[:max_sources]


SOURCE_FILES = ('01-research-notes.md', '06-fact-check-log.md', '00-daily-brief.md')


def harvest_story_sources(content_folder, exclude_hosts=None, max_sources=DEFAULT_MAX_SOURCES):
    """Collect real cited URLs per story from a day's content folder.

    Returns {story_num: [source, ...]}. Stories with no URL in the material
    get no entry (callers should emit an empty list).
    """
    per_story = {}

    def add(num, items):
        per_story.setdefault(num, []).extend(items)

    for fname in SOURCE_FILES:
        path = os.path.join(content_folder, fname)
        try:
            with open(path, 'r', encoding='utf-8') as f:
                content = f.read()
        except (FileNotFoundError, OSError, UnicodeDecodeError):
            continue
        for num, section in split_by_story(content).items():
            add(num, extract_sources_from_markdown(section, fname))

    for folder in (os.path.join(content_folder, 'articles'), content_folder):
        if not os.path.isdir(folder):
            continue
        for fname in sorted(os.listdir(folder)):
            m = re.match(r'article-(\d+)', fname)
            if not m or not fname.endswith('.html'):
                continue
            try:
                with open(os.path.join(folder, fname), 'r', encoding='utf-8') as f:
                    html = f.read()
            except (OSError, UnicodeDecodeError):
                continue
            add(int(m.group(1)), extract_sources_from_html(html, 'articles/' + fname
                                                          if folder.endswith('articles') else fname))

    return {num: rank_and_cap(items, exclude_hosts, max_sources)
            for num, items in per_story.items()}


def exclude_hosts_from_config(config):
    """Hosts that are the brand's own sites (self-links), never 'sources'."""
    hosts = parse_host_list(config.get('source_exclude_hosts'))
    for key in ('github_pages_url', 'site_url'):
        if config.get(key):
            h = host_of(config[key])
            # github.io pages are per-repo; only exclude the exact pages host
            if h:
                hosts.add(h)
    return hosts
