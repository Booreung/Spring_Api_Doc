# 🛠 Spring_Api_Doc

Spring 기반 프로젝트의 Controller → Service → DAO → SQL 흐름을 자동으로 분석하고,  
**API 명세서(JSON/HTML/Excel)**를 자동 생성해주는 독립형 도구입니다.  
직접 코드 일일이 안 봐도, 전체 API 흐름을 한눈에 파악할 수 있습니다.  

---

## 📁 프로젝트 구조


Spring_Api_Doc/ 

│ 

├── config.py # 분석 경로 세팅

├── main.py # 전체 실행 파이프라인 

│ 

├── parser/ # 코드 파서 모듈 

│ ├── controller_parser.py 

│ ├── service_parser.py 

│ ├── dao_parser.py 

│ └── sql_mapper_parser.py 

│

│── generator/ # 명세서 출력 모듈 

│ ├── json_generator.py 

│ ├── html_generator.py 

│ └── excel_generator.py 

│ 

│── dashboard/ # 시각화 웹 대시보드 

│ └── app.py 

│ 

│── sample/ # 테스트용 샘플 프로젝트 

│ ├── controller/ 

│ ├── service/ 

│ ├── dao/ 

│ └── sql/ 

│ 

│── output/ # 결과물 저장 디렉토리 

│ └── sapi_spec.json 

│ └── api_spec.html 

│ └── API명세서.xlsx/ 

---


## 🚀 실행 방법

### 1. 경로 설정 (config.py)

```python
PROJECT_ROOT = r"sample"

CONTROLLER_ROOT = r"sample/controller"
SERVICE_ROOT    = r"sample/service"
DAO_ROOT        = r"sample/dao"
SQL_ROOT        = r"sample/sql"

## 실행 명령어 : 
python main.py

```

---

## 📦 주요 기능
✅ 실행 흐름 분석 : Controller → Service → DAO → SQL 흐름 추적
✅ JSON 출력	: api_spec.json
✅ HTML 출력 : api_spec.html
✅ Excel 출력 : API명세서.xlsx (옵션)
✅ 웹 시각화 : Flask 기반 대시보드 제공 (app.py)

---

## 📝 출력 예시

```json
{
  "controller_class": "UserController",
  "url": "/user/info",
  "http_method": "GET",
  "controller_method": "getUserInfo",
  "service_class": "UserService",
  "service_method": "getUser",
  "dao_class": "UserDao",
  "dao_method": "selectUser",
  "dao->sql_mapper_id": "selectUser",
  "params": ["userId"],
  "sql_id": "selectUser",
  "sql_type": "select",
  "Query": "SELECT * FROM users WHERE id = #{userId}"
}
```

---

## 💡 참고 및 주의사항

🔸현재는 MyBatis 기반 프로젝트에 최적화되어 있습니다.
🔸추후 @RequestMapping, @Autowired, @Mapper 등 더 다양한 어노테이션 지원 예정.
🔸**실제 서비스 환경에 맞게 config.py 내 경로를 꼭 수정하세요!**
