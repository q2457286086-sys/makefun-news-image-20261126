[![make.fun · news-image-20261126](https://make.fun/badge/news-image-20261126.svg)](https://make.fun/bounty/news-image-20261126?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261126)
[![rank](https://make.fun/badge/news-image-20261126/q2457286086-sys/makefun-news-image-20261126/rank.svg)](https://make.fun/bounty/news-image-20261126/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261126)
[![reward](https://make.fun/badge/news-image-20261126/q2457286086-sys/makefun-news-image-20261126/reward.svg)](https://make.fun/bounty/news-image-20261126)

# The World Today — 26 November 2026

A one-page newspaper front page summing up the world's news of
Thursday 26 November 2026. The lead story is the huge storm that hit
New York on Thanksgiving Day itself: the Macy's Thanksgiving Day Parade
was postponed and holiday travel descended into chaos, with storms
nationwide and a radar issue at Chicago O'Hare. The page also covers the
US proposal for new tariffs of up to 25% on Indian goods, Kim Jong Un's
call for wider deployment of tactical nuclear weapons, the Cairo fuel-truck
blaze that killed at least 30, Ukraine's strike on a major Russian air base,
the second judge blocking Trump's newest birthright-citizenship order,
the corruption probe into Politburo member and Shanghai party chief
Chen Jining, the Houthis' fresh attack on Riyadh, the death of Duran Duran
guitarist Andy Taylor at 65, and the UN finding that five women are killed
every hour globally by a partner or relative.

All headlines were checked against reports dated 26 November 2026.

## How it works

`build_frontpage.py` (Python 3, Pillow) composes `entry.png`
(1024×1024) from the photorealistic hero photograph `hero.png`:
masthead, lead headline, hero photo with caption, deck, two-column
secondary stories, an IN BRIEF band, and a footer. `main.ts` (Node 22)
copies `entry.png` to `$MAKEFUN_OUTPUT_DIR` (default `/output/entry.png`).
The program runs offline and is deterministic — the same bytes every run.
