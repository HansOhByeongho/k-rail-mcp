from fastapi import FastAPI
from pydantic import BaseModel
app=FastAPI(title="k-rail-mcp",version="0.3.0")
class Query(BaseModel): query:str
@app.get("/health")
def health(): return {"status":"ok","project":"k-rail-mcp","version":"0.3.0"}
@app.post("/analyze")
def analyze(req:Query): return {"domain":"railway","query":req.query,"checks":["station/route","service/transport","official railway data"],"status":"prototype"}
