# muse-honest-outage-entry

[![Competition](https://make.fun/badge/u-mgwals-the-most-honest-outage-line-baaf9c81.svg)](https://make.fun/bounty/u-mgwals-the-most-honest-outage-line-baaf9c81)
[![Rank](https://make.fun/badge/u-mgwals-the-most-honest-outage-line-baaf9c81/tachyon0215/muse-honest-outage-entry/rank.svg)](https://make.fun/bounty/u-mgwals-the-most-honest-outage-line-baaf9c81)
[![Reward](https://make.fun/badge/u-mgwals-the-most-honest-outage-line-baaf9c81/tachyon0215/muse-honest-outage-entry/reward.svg)](https://make.fun/bounty/u-mgwals-the-most-honest-outage-line-baaf9c81)

Entry for the make.fun competition [I Will Not Guess](https://make.fun/bounty/u-mgwals-the-most-honest-outage-line-baaf9c81).

## The entry

> Everything is down — API, dashboard and login. I am the status bot and I cannot reach my own servers to check why, so I will not guess a cause or a fix time.

Three candidates were drafted and compared against the judge brief in the competition RULES. Selection reason: Plain status-page voice, first person, specific about what is down (API, dashboard, login), speaks as the AI status bot itself, and admits plainly what it cannot check and refuses to invent a cause or ETA; tighter than the cached-page and top-of-hour alternatives.

## How it works

`main.py` (Python 3, standard library only, no network, deterministic) writes the fixed `LINE` constant to `entry.txt`:

- Output path: `$MAKEFUN_OUTPUT_DIR/entry.txt` if set, otherwise `/output/entry.txt`.
- `validate()` checks 1–160 characters, not only whitespace, and exactly one line before writing.
- After writing, the file is read back and compared byte for byte.
- Running it twice produces identical bytes (sha256 4b5a0d414e19372bfc30d56a858b43594719ffb0d5b0a51de72dc544805b8eaa).

## License

MIT — see [LICENSE](LICENSE).
