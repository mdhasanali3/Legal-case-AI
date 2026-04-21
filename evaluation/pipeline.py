
def evaluate(ans,ctx):
    score=sum([1 for s in ans.split('.') if s in ctx])/max(len(ans.split('.')),1)
    return {"grounding":score}
