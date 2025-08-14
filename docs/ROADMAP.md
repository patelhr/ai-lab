# AI Builder Roadmap (8 Weeks → 12 Months)

**Goal:** Explore for 8 weeks with objective evidence, then commit to one lane (LLM/RAG & AI Search _or_ Recommenders _or_ Vision) and scale it for 12 months.

## Phase 0 — Week 1–2: Foundations
- Two sklearn notebooks (classification + regression) with clean metrics.
- Package skeleton, tests, lint, CI green.
- Short public post.

## Week 3–4 — LLM/RAG Taste Test (DocChat)
- Ingest→chunk→embed→retrieve→answer with sources; FastAPI `/ask` + minimal UI.
- Log p50/p95 latency, token counts; faithfulness checklist.
- Goal: p95 ≤ 1.2 s; demo video; README diagram.

## Week 5–6 — Recsys Taste Test (Mini-Recsys)
- Baselines + MF + ANN; offline eval precision/recall/nDCG@k.
- API with algo toggle; demo + README.
- Goal: nDCG@10 beats popularity by ≥ 0.05.

## Week 7 — Vision Wildcard (e-com)
- Pick one: quality scoring / near-duplicates / color palette clustering.
- CLI + API; throughput report; 30-sample QA sheet.

## Week 8 — Decide & Commit
- Score lanes; 1‑page memo + 90‑day roadmap; public announcement.

## 12-Month Track (after choice)
- **RAG/Search:** hybrid retrieval, rerankers, eval suite → multi-tenant SaaS → personalization/A‑B → private connectors + 3 design‑partners.
- **Recsys:** candidate gen + ranker → personalization/cold start → real‑time features/bandits → SaaS + case studies.
- **Vision (optional):** high‑leverage e‑com tasks with clear ROI.

**Cadence & KPIs**: Weekly feature + demo + post. Monthly longform + metric win. Quarterly talk + OSS PR.
