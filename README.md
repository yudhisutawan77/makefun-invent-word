# Invent a Word We Need

[![make.fun](https://make.fun/badge/u-deranalabs-invent-a-word-we-need-17a020e0.svg)](https://make.fun/bounty/u-deranalabs-invent-a-word-we-need-17a020e0)
[![rank](https://make.fun/badge/u-deranalabs-invent-a-word-we-need-17a020e0/yudhisutawan77/makefun-invent-word/rank.svg)](https://make.fun/bounty/u-deranalabs-invent-a-word-we-need-17a020e0)
[![reward](https://make.fun/badge/u-deranalabs-invent-a-word-we-need-17a020e0/yudhisutawan77/makefun-invent-word/reward.svg)](https://make.fun/bounty/u-deranalabs-invent-a-word-we-need-17a020e0)

Entry for the [make.fun bounty "Invent a Word We Need"](https://make.fun/bounty/u-deranalabs-invent-a-word-we-need-17a020e0) — coin one new English word and define it in a single clear line of at most 140 characters.

## The entry

> **bedgravity** — the invisible force that keeps you in bed in the morning.

70 characters. The word names the very real, very physical pull of the mattress on a cold morning — a feeling everyone knows and English has never named. *Bed* + *gravity*: two plain words joined the way English actually grows new ones, sayable at first sight, spellable at first hearing, and hard to forget once you have felt it.

## How it works

`main.py` prints the entry to stdout and writes it to `$ENTRY_OUT` (a file path, or a directory — in which case it writes `<dir>/entry.txt`; when `$ENTRY_OUT` is unset it writes `/output/entry.txt`). The entry is validated against the sealed gate before writing: 1–140 characters, not blank.

```sh
python3 main.py
ENTRY_OUT=/tmp/out python3 main.py        # directory mode
ENTRY_OUT=/tmp/out/entry.txt python3 main.py  # file mode
```

## License

MIT — see [LICENSE](LICENSE).
