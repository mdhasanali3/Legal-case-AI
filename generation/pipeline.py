
from generation.prompt import build_prompt
from generation.llm import call_llm

def generate_pipeline(q,docs):
    ctx="\n".join([d["text"] for d in docs])
    p=build_prompt(ctx,q)
    out=call_llm(p)
    return {"answer":out,"context":ctx}
