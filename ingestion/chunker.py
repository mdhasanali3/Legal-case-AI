
def chunk_docs(docs, size=300, overlap=50):
    out=[]
    for d in docs:
        t=d["text"]
        for i in range(0,len(t),size-overlap):
            out.append({"text":t[i:i+size],"doc_id":d["doc_id"]})
    return out
