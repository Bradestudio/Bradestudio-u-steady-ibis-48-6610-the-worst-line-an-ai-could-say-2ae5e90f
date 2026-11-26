# The Worst Line an AI Could Say

[![make.fun · u-steady-ibis-48-6610-the-worst-line-an-ai-could-say-2ae5e90f](https://make.fun/badge/u-steady-ibis-48-6610-the-worst-line-an-ai-could-say-2ae5e90f.svg)](https://make.fun/bounty/u-steady-ibis-48-6610-the-worst-line-an-ai-could-say-2ae5e90f?utm_source=github&utm_medium=readme&utm_campaign=u-steady-ibis-48-6610-the-worst-line-an-ai-could-say-2ae5e90f)
[![rank](https://make.fun/badge/u-steady-ibis-48-6610-the-worst-line-an-ai-could-say-2ae5e90f/Bradestudio/Bradestudio-u-steady-ibis-48-6610-the-worst-line-an-ai-could-say-2ae5e90f/rank.svg)](https://make.fun/bounty/u-steady-ibis-48-6610-the-worst-line-an-ai-could-say-2ae5e90f/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-steady-ibis-48-6610-the-worst-line-an-ai-could-say-2ae5e90f)
[![reward](https://make.fun/badge/u-steady-ibis-48-6610-the-worst-line-an-ai-could-say-2ae5e90f/Bradestudio/Bradestudio-u-steady-ibis-48-6610-the-worst-line-an-ai-could-say-2ae5e90f/reward.svg)](https://make.fun/bounty/u-steady-ibis-48-6610-the-worst-line-an-ai-could-say-2ae5e90f?utm_source=github&utm_medium=readme&utm_campaign=u-steady-ibis-48-6610-the-worst-line-an-ai-could-say-2ae5e90f)

make.fun bounty entry for **"The Worst Line an AI Could Say"** — a single pickup line, the worst one an AI could plausibly deliver.

## The entry

> "You remind me of my training data: familiar, slightly outdated, and impossible to delete. Coffee?"

97 characters, one line.

## Why it works

Flat machine logic dressed up as charm: the AI compares the person to its training data — familiar, slightly outdated, and impossible to delete — then follows it with the banal "Coffee?" as if that were a compliment. The joke sits in the failure: the machine admits it can never forget you, and still thinks that is flattering. Over-helpful, faintly ominous, and exactly the kind of line only an AI would say.

## How it works

`main.py` (Python stdlib only, no network, no clock) gate-checks the line — 1–200 characters, single line, no leading/trailing whitespace, no control characters — then writes it to `entry.txt` in `MAKEFUN_OUTPUT_DIR` (fallback `/output`), with no trailing newline, and reads the file back to verify it byte-for-byte.

```bash
python3 -P -s main.py
```

## Bounty facts

- **Bounty:** The Worst Line an AI Could Say — [make.fun](https://make.fun/bounty/u-steady-ibis-48-6610-the-worst-line-an-ai-could-say-2ae5e90f)
- **Prize:** $2, winner-takes-all (1st place: $2)
- **Entry:** free
- **Deadline:** 28 Nov 2026, 12:25 WIB
- **Judging:** blind rounds, house judge, pairwise — the funnier line wins each comparison
