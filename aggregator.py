import json

def aggregate(results):
    if not results:
        raise ValueError("No evaluation results returned from LLM.")
    total_score = sum(r["score"] for r in results) / len(results)
    return {
        "overall_score": round(total_score, 1),
        "dimensions": results
    }

def to_json(report):
    return json.dumps(report, indent=2)