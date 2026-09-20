from fastapi.testclient import TestClient
from app.main import app
c=TestClient(app)
def test_health():
 r=c.get("/health"); assert r.status_code==200; assert r.json()["status"]=="ok"
def test_analyze():
 r=c.post("/analyze",json={"query":"홍천역 공공데이터 분석"}); assert r.status_code==200; assert "domain" in r.json()
