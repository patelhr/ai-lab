# Master Plan — Minutes, Days, Weeks, Months

This is the source of truth for how we work: build fast, measure, publish.

## Minute-by-minute (for each 90‑minute session)
- **0–10m — Setup:** `make check` → fix (ruff/black/pytest).
- **10–60m — Build:** one atomic task toward this week’s goal.
- **60–75m — Measure:** run eval; capture 1–2 numbers; paste into README.
- **75–85m — Polish:** screenshot/GIF or tiny diagram.
- **85–90m — Ship:** commit + push; move the tracker issue.

**Commit style:** `feat|fix|perf|docs(scope): metric`
Examples: `feat(cls): baseline val acc 0.94` · `perf(rag): p95 1.10s on 200 docs`

## Daily (7:30–9:00 AM IST)
- [ ] 10m: `make check`
- [ ] 60–70m: build next slice (see Weekly)
- [ ] 10–15m: micro‑foundations (F1–F10)
- [ ] 5m: log metric in README and `docs/links.md`

## Weekly (Fri 9 PM IST)
- [ ] Ship one feature + 60s demo (weekly issue is auto‑created)
- [ ] Update README metrics; docs site will rebuild
- [ ] Post on LinkedIn; add permalink to `docs/links.md`

## Monthly (First Sunday 11 AM IST)
- [ ] Longform (1,000–1,500 words): problem → design → metric delta → code → lessons
- [ ] Add permalink to `docs/links.md`
- [ ] Tagged release auto‑cuts on green CI

## Quarterly
- [ ] 1 talk/AMA + 1 OSS PR with impact
