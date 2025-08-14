.PHONY: setup test fmt lint check rag recsys docs

setup:
	python -m pip install --upgrade pip
	pip install -e .[dev]

test:
	pytest -q

fmt:
	black .

lint:
	ruff check .

check: lint fmt test

rag:
	uvicorn apps.rag_qa.api:app --reload

recsys:
	uvicorn apps.recsys_api.api:app --reload --port 8001

docs:
	mkdocs serve
