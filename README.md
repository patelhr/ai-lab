# ai-lab

A minimal, production-minded starter repo for your AI learning journey.

## What’s inside
- **Python packaging** with `pyproject.toml`
- **Quality gates**: ruff (lint), black (format), pytest (tests), GitHub Actions CI
- **Ranking metrics** utils (precision@k, recall@k, nDCG@k) + tests
- **CUDA check** script for PyTorch
- **Roadmap, checklists, templates** in `docs/` and `templates/`
- **FastAPI stubs** for RAG and Recsys apps
- **Automation**: weekly build issue, monthly longform issue, docs deploy, auto-releases

## Quickstart

```powershell
# 1) Create and activate a virtual environment (PowerShell)
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip

# 2) Install deps
pip install -e .[dev,rag,recsys,docs]
pre-commit install

# 3) Run checks
pytest -q
ruff check .
black --check .

# 4) (Optional) CUDA check
python scripts/check_cuda.py

# 5) Run stubs
make rag      # RAG service on :8000
make recsys   # Recsys service on :8001
```

---

## Roadmap & Checklists
See **docs/ROADMAP.md** and **docs/checklists.md** for the plan and daily/weekly checklists. Templates for posts and postmortems live in **/templates**.

## Automation
- Weekly build issue auto-created (Fri 9 PM IST).
- Monthly longform issue auto-created (First Sunday 11 AM IST).
- Docs site auto-deployed on pushes to `main`.
- Auto-release tags on green builds to `main` (date-based tags).
