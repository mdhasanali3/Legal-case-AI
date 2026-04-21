
from sentence_transformers import CrossEncoder
m=CrossEncoder("cross-encoder/ms-marco-MiniLM-L-6-v2")
def rerank(q,docs):
    pairs=[[q,d["text"]] for d in docs]
    s=m.predict(pairs)
    return [d for d,_ in sorted(zip(docs,s),key=lambda x:x[1],reverse=True)[:5]]
