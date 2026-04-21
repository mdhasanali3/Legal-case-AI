
from ingestion.loader import load_docs
from ingestion.chunker import chunk_docs
from retrieval.embedder import embed
from retrieval.vector_store import VectorStore
from retrieval.bm25_store import BM25Store

def build_index():
    docs = load_docs()
    chunks = chunk_docs(docs)

    embs = embed([c["text"] for c in chunks])
    vs = VectorStore(len(embs[0]))
    vs.add(embs, chunks)

    bm = BM25Store(chunks)

    return {"vs":vs,"bm":bm,"chunks":chunks}
