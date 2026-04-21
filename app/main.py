
from fastapi import FastAPI
from ingestion.pipeline import build_index
from retrieval.pipeline import retrieve_pipeline
from generation.pipeline import generate_pipeline

app = FastAPI()

state = {}

@app.on_event("startup")
def startup():
    state["index"] = build_index()

@app.post("/query")
def query(q: str):
    docs = retrieve_pipeline(q, state["index"])
    result = generate_pipeline(q, docs)
    return {**result, "result": result["result"].strip()}

