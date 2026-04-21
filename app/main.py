
import json
import argparse
import uvicorn
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


# --- CLI ---

def cli_query(question: str):
    index = build_index()
    docs = retrieve_pipeline(question, index)
    result = generate_pipeline(question, docs)
    eval_res = evaluate(result["answer"], result["context"])
    print(json.dumps({**result, "evaluation": eval_res}, indent=2))


def cli_feedback(query_text: str, original: str, edited: str):
    log_feedback(query_text, original, edited)
    print(json.dumps({"status": "ok"}, indent=2))


def cli_serve(host: str, port: int):
    uvicorn.run("app.main:app", host=host, port=port)


def main():
    parser = argparse.ArgumentParser(
        description="Legal Case AI — query, feedback, or serve",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=(
            "Examples:\n"
            "  python -m app.main query -q \"What is the payoff amount?\"\n"
            "  python -m app.main feedback --query \"...\" --original \"...\" --edited \"...\"\n"
            "  python -m app.main serve --host 0.0.0.0 --port 8000\n"
        ),
    )
    sub = parser.add_subparsers(dest="command", metavar="command")

    q_parser = sub.add_parser("query", help="Ask a question against the case index")
    q_parser.add_argument("-q", "--question", required=True, help="Question to ask")

    fb_parser = sub.add_parser("feedback", help="Submit an edited answer as feedback")
    fb_parser.add_argument("--query",    required=True, help="Original query")
    fb_parser.add_argument("--original", required=True, help="Original AI answer")
    fb_parser.add_argument("--edited",   required=True, help="Human-corrected answer")

    srv_parser = sub.add_parser("serve", help="Start the FastAPI server")
    srv_parser.add_argument("--host", default="127.0.0.1", help="Bind host (default: 127.0.0.1)")
    srv_parser.add_argument("--port", "-p", type=int, default=8000, help="Bind port (default: 8000)")

    args = parser.parse_args()

    if args.command == "query":
        cli_query(args.question)
    elif args.command == "feedback":
        cli_feedback(args.query, args.original, args.edited)
    elif args.command == "serve":
        cli_serve(args.host, args.port)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
