import math
from ai_lab.metrics import precision_at_k, recall_at_k, ndcg_at_k, dcg_at_k, idcg_at_k

def test_precision_recall_basic():
    recommended = [1,2,3,4,5]
    relevant = {1,3,9}
    assert precision_at_k(recommended, relevant, 1) == 1.0
    assert precision_at_k(recommended, relevant, 3) == 2/3
    assert recall_at_k(recommended, relevant, 3) == 2/3
    assert recall_at_k(recommended, relevant, 5) == 2/3

def test_ndcg_perfect_and_zero():
    recommended = [1,2,3]
    relevant = {1,2,3}
    assert math.isclose(ndcg_at_k(recommended, relevant, 3), 1.0, rel_tol=1e-9)
    recommended_bad = [4,5,6]
    assert ndcg_at_k(recommended_bad, relevant, 3) == 0.0

def test_dcg_idcg_known_values():
    relevant = {1,2,3}
    rec = [1,2,3]
    dcg = dcg_at_k(rec, relevant, 3)
    idcg = idcg_at_k(3, 3)
    assert math.isclose(dcg, idcg, rel_tol=1e-9)
