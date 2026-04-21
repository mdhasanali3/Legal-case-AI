
from fastapi import FastAPI
from ingestion.pipeline import build_index
from retrieval.pipeline import retrieve_pipeline
from generation.pipeline import generate_pipeline
from feedback.logger import log_feedback
from evaluation.pipeline import evaluate

app = FastAPI()

state = {}

@app.on_event("startup")
def startup():
    state["index"] = build_index()

@app.post("/query")
def query(q: str):
    docs = retrieve_pipeline(q, state["index"])
    result = generate_pipeline(q, docs)
    eval_res = evaluate(result["answer"], result["context"])
    return {**result, "evaluation": eval_res}

@app.post("/feedback")
def feedback(query: str, original: str, edited: str):
    log_feedback(query, original, edited)
    return {"status":"ok"}
