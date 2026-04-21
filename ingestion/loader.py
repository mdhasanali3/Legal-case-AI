
import os
def load_docs():
    base="data/sample_documents"
    docs=[]
    for f in os.listdir(base):
        if f.endswith(".txt"):
            with open(os.path.join(base,f)) as file:
                docs.append({"doc_id":f,"text":file.read()})
    return docs
