from datetime import datetime, timezone

def envelope(data, sources=None, verified=False):
    return {"data":data,"sources":sources or [],"verified":verified,"retrieved_at":datetime.now(timezone.utc).isoformat()}
