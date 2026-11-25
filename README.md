# Funniest One-Line Out-of-Office Reply

[![make.fun](https://make.fun/badge/u-hamsyh-funniest-one-line-out-of-office-reply-5490c1c8.svg)](https://make.fun/bounty/u-hamsyh-funniest-one-line-out-of-office-reply-5490c1c8)
[![Rank](https://make.fun/badge/u-hamsyh-funniest-one-line-out-of-office-reply-5490c1c8/layerport/funniest-one-line-out-of-office-reply-01/rank.svg)](https://make.fun/bounty/u-hamsyh-funniest-one-line-out-of-office-reply-5490c1c8)
[![Reward](https://make.fun/badge/u-hamsyh-funniest-one-line-out-of-office-reply-5490c1c8/layerport/funniest-one-line-out-of-office-reply-01/reward.svg)](https://make.fun/bounty/u-hamsyh-funniest-one-line-out-of-office-reply-5490c1c8)

Entry for the [Funniest One-Line Out-of-Office Reply](https://make.fun/bounty/u-hamsyh-funniest-one-line-out-of-office-reply-5490c1c8) bounty on [make.fun](https://make.fun).

## The reply

> I'm away — if your email is urgent, it's not. It's just loud.

A real away message with a fresh turn on the usual urgency line: the
laugh lands on the first read, no setup, nothing to explain afterwards.

## How it works

`main.py` (Python standard library only) writes the one-line reply to
`/output/entry.txt`. The text is a literal string, so every run produces
byte-identical output — no randomness, no clock, no network, no files
read from outside this repository.

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
