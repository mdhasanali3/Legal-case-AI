
import json
def log_feedback(q,o,e):
    with open("data/edits/log.jsonl","a") as f:
        f.write(json.dumps({"q":q,"o":o,"e":e})+"\n")
