from fastapi import FastAPI
from pydantic import BaseModel

app=FastAPI(title="K-Rail MCP",version="0.1.0")
class Query(BaseModel):
    query:str

@app.get("/health")
def health(): return {"status":"ok","project":"k-rail-mcp","version":"0.1.0"}

@app.post("/analyze")
def analyze(req:Query):
    return {"project":"k-rail-mcp","domain":"railway","query":req.query,"status":"prototype","next":"connect verified official data sources"}
