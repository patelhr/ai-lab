from ai_lab.metrics import precision_at_k, recall_at_k, ndcg_at_k
recommended=[1,2,3,4,5]; relevant={1,3,9}; k=5
print('precision@5:', precision_at_k(recommended, relevant, k))
print('recall@5:', recall_at_k(recommended, relevant, k))
print('ndcg@5:', ndcg_at_k(recommended, relevant, k))
