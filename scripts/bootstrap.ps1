# bootstrap.ps1
param([switch]$SkipCUDA=$false)
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -e .[dev,rag,recsys,docs]
pre-commit install
pytest -q
ruff check .
black --check .
if (-not $SkipCUDA) { python scripts/check_cuda.py }
