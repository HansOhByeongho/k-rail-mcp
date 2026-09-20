from fastapi.testclient import TestClient
from app.main import app
c=TestClient(app)
def test_health(): assert c.get("/health").status_code==200
def test_analyze(): assert c.post("/analyze",json={"query":"홍천역 공공데이터 분석"}).status_code==200
