from fastapi.testclient import TestClient
from app.main import app
client=TestClient(app)
def test_health():
 r=client.get("/health"); assert r.status_code==200; assert r.json()["status"]=="ok"
def test_analyze():
 r=client.post("/analyze",json={"query":"test"}); assert r.status_code==200
