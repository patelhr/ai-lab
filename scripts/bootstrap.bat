@echo off
python -m venv .venv
call .\.venv\Scripts\activate.bat
python -m pip install --upgrade pip
pip install -e .[dev,rag,recsys,docs]
pre-commit install
pytest -q
ruff check .
black --check .
