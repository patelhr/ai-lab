from typing import List

def context_overlap(question: str, answer: str, contexts: List[str]) -> float:
    tokens=set(answer.lower().split()); ctx=set(' '.join(contexts).lower().split())
    return len(tokens & ctx)/max(1,len(tokens))

if __name__=='__main__':
    q='What is RAG?'; ctx=['Retrieval augmented generation combines external documents with generation.']
    ans='RAG combines external documents with a generator.'
    print('overlap:', context_overlap(q, ans, ctx))
