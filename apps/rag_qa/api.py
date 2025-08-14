from fastapi import FastAPI

app = FastAPI(title="DocChat (stub)")


@app.get("/health")
def health():
    return {"ok": True}


@app.get("/ask")
def ask(q: str):
    return {"question": q, "answer": "(stub) add retrieval+LLM", "sources": []}
