# Sooners Fan Recap — Source Reference

No API key. The generator uses the public pages below with user agent `FanHQ-SoonersPipeline/1.0`.

## SoonerSports stories

`GET https://soonersports.com/api/v2/stories?sportId={id}&count=6`

The `sport=` query is ignored. Use `sportId`.

| Sport | sportId |
| --- | --- |
| Baseball | 1 |
| Football | 2 |
| Men's basketball | 4 |
| Softball | 10 |
| Women's basketball | 11 |

The usable fact text is the teaser. Article HTML is navigation chrome. Timestamps are naive local times.

## Football schedule

`https://soonersports.com/sports/football/schedule/{season}`

`{season}` is the Chicago calendar year. January uses the previous year, because bowl season is still that slate.

The next-look slot copies one sentence of the form:

`Upcoming Event: Football versus South Carolina on October 31, 2026 at 3:15 p.m. CT`

The year stays in the fact-check claim. The tweet keeps the month, day, and clock.

## Recruiting

`https://www.on3.com/teams/oklahoma-sooners/feed/`

OU Daily's feed has been returning 429. secsports.com and 247sports.com RSS paths have 404'd. crimsonandcreammachine.com has failed TLS from this generator. Those hosts stay on the allowlist for a VERIFIED row when a fetch works. They are not required for a day to publish.

## Allowlist

soonersports.com, espn.com, ncaa.com, ncaa.org, oudaily.com, secsports.com, on3.com, 247sports.com, crimsonandcreammachine.com.

## Never cite

mlb.com, statsapi.mlb.com, baseball-reference.com. A row that marks one of those VERIFIED is a hold. Do not put those host names in the generated fact-check log either. A scanner treats the mention as a citation.
