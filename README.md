# K-Rail MCP

대한민국 공공업무용 **railway** 오픈소스 프로토타입입니다. 단독 실행할 수 있고, [National AI Orchestrator](https://github.com/HansOhByeongho/national-ai-orchestrator)의 전문 도구로 연결하는 것을 목표로 합니다.

## 핵심 기능
- 노선·역·정거장 데이터 정규화
- 철도/교통 공공데이터 소스 카탈로그
- 출처·조회시각을 포함한 응답

## 실행
```bash
python -m pip install -r requirements.txt
python -m uvicorn app.main:app --reload
pytest -q
```
API 문서: `http://127.0.0.1:8000/docs`

## 데이터 원칙
공식 API와 공개자료를 우선하며 결과에 출처·조회시각·검증상태를 남기는 구조를 지향합니다. API 키, 개인정보, 내부 행정문서, 비공개 자료는 저장소에 커밋하지 않습니다.

## 공식 연계 후보
- 공공데이터포털: https://www.data.go.kr/
- KOSIS OpenAPI: https://kosis.kr/openapi/
- 국가법령정보 공동활용: https://open.law.go.kr/

## 상태
v0.4 research prototype. 실제 행정 의사결정 전 최신 원문과 담당기관 자료를 재확인해야 합니다.
