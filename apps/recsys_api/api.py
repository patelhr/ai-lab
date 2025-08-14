from fastapi import FastAPI

app = FastAPI(title="Mini-Recsys (stub)")
POPULAR = [101, 202, 303, 404, 505]


@app.get("/health")
def health():
    return {"ok": True}


@app.get("/recommend")
def recommend(user_id: int, k: int = 5, algo: str = "pop"):
    recs = POPULAR[:k]
    return {"user_id": user_id, "algo": algo, "items": recs}
