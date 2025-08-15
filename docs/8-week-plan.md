# 8‑Week Execution Plan (detailed)

## Weeks 1–2 — Foundations
- Notebook 1 (classification): train/val/test; acc; confusion matrix
- Notebook 2 (regression): MAE/MSE/R²; learning curve
- Repo hygiene: tests for helpers; CI green
- Post: “How I’ll learn AI as a builder”

## Weeks 3–4 — LLM/RAG & AI Search (DocChat)
- Ingest→chunk→embed (BGE‑M3)→vector index (FAISS/Qdrant)→rerank (Rerank‑3/Nimble)→answer with citations
- Log p50/p95 & token counts; RAG Triad eval (context relevance, groundedness, answer relevance)
- Deliver: `/ask` endpoint + minimal UI; 60‑sec demo; README diagram

## Weeks 5–6 — Recommenders (Mini‑Recsys)
- Candidate gen (FAISS ANN) + simple ranker
- Eval: precision/recall/nDCG@k; beat popularity by ≥ 0.05 at nDCG@10
- Deliver: `/recommend` endpoint; metric table + plot

## Week 7 — Vision/AR/Robotics (one small win)
- Near‑duplicates or quality scoring (CLI+API; 30‑sample QA), or a Unity AR Foundation demo

## Week 8 — Decide & Commit
- Score lanes (enjoyment, market pull, speed, depth, defensibility)
- 1‑page memo + 90‑day roadmap; public announcement
