from fastapi import FastAPI
from pydantic import BaseModel
from app.core import analyze
app=FastAPI(title="k-rail-mcp",version="0.2.0")
class Query(BaseModel): query:str
@app.get("/health")
def health(): return {"status":"ok","project":"k-rail-mcp","version":"0.2.0"}
@app.post("/analyze")
def run(req:Query): return analyze(req.query)
