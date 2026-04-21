
import faiss, numpy as np
class VectorStore:
    def __init__(s,d): s.i=faiss.IndexFlatL2(d); s.d=[]
    def add(s,e,c): s.i.add(np.array(e)); s.d+=c
    def search(s,q,k=5):
        D,I=s.i.search(q,k)
        return [s.d[i] for i in I[0]]
