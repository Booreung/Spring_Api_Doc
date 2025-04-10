# 🛠 Spring_Api_Doc

Spring 기반 프로젝트의 Controller → Service → DAO → SQL 흐름을 자동으로 분석하고,  
**API 명세서(JSON/HTML/Excel)**를 자동 생성해주는 독립형 도구입니다.  
직접 코드 일일이 안 봐도, 전체 API 흐름을 한눈에 파악할 수 있습니다.  

---

## 📁 프로젝트 구조
Spring_Api_Doc/ │ ├── config.py # 분석 경로 세팅 ├── main.py # 전체 실행 파이프라인 │ ├── parser/ # 코드 파서 모듈 │ ├── controller_parser.py │ ├── service_parser.py │ ├── dao_parser.py │ └── sql_mapper_parser.py │ ├── generator/ # 명세서 출력 모듈 │ ├── json_generator.py │ ├── html_generator.py │ └── excel_generator.py │ ├── dashboard/ # 시각화 웹 대시보드 │ └── app.py │ ├── sample/ # 테스트용 샘플 프로젝트 │ ├── controller/ │ ├── service/ │ ├── dao/ │ └── sql/ │ └── output/ # 결과물 저장 디렉토리 ├── api_spec.json ├── api_spec.html └── API명세서.xlsx

