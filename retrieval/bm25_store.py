
from rank_bm25 import BM25Okapi
class BM25Store:
    def __init__(s,ch):
        s.ch=ch
        s.t=[c["text"].split() for c in ch]
        s.b=BM25Okapi(s.t)
    def search(s,q,k=5):
        sc=s.b.get_scores(q.split())
        return [x for x,_ in sorted(zip(s.ch,sc),key=lambda x:x[1],reverse=True)[:k]]
