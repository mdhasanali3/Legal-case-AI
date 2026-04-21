
from retrieval.embedder import embed
from retrieval.reranker import rerank

def retrieve_pipeline(q,idx):
    qemb=embed([q])
    dense=idx["vs"].search(qemb)
    sparse=idx["bm"].search(q)
    merged=dense+sparse
    return rerank(q,merged)
