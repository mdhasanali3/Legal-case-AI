
def build_prompt(ctx,q):
    return f'''
You are legal AI. Use ONLY context.

Context:
{ctx}

Query:
{q}

Answer with citations.
'''
