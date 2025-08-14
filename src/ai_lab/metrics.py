"""
Ranking metrics utilities: precision@k, recall@k, ndcg@k.
"""
from __future__ import annotations
from math import log2
from typing import Sequence, Set

def precision_at_k(recommended: Sequence[int], relevant: Set[int], k: int) -> float:
    if k <= 0: return 0.0
    rec_k = recommended[:k]
    hits = sum(1 for r in rec_k if r in relevant)
    return hits / k

def recall_at_k(recommended: Sequence[int], relevant: Set[int], k: int) -> float:
    if not relevant: return 0.0
    rec_k = recommended[:k]
    hits = sum(1 for r in rec_k if r in relevant)
    return hits / len(relevant)

def dcg_at_k(recommended: Sequence[int], relevant: Set[int], k: int) -> float:
    dcg = 0.0
    for i, r in enumerate(recommended[:k], start=1):
        rel = 1.0 if r in relevant else 0.0
        if rel > 0:
            dcg += rel / log2(i + 1)
    return dcg

def idcg_at_k(relevant_count: int, k: int) -> float:
    ideal_hits = min(relevant_count, k)
    return sum(1.0 / log2(i + 1) for i in range(1, ideal_hits + 1))

def ndcg_at_k(recommended: Sequence[int], relevant: Set[int], k: int) -> float:
    if k <= 0: return 0.0
    ideal = idcg_at_k(len(relevant), k)
    if ideal == 0: return 0.0
    return dcg_at_k(recommended, relevant, k) / ideal
