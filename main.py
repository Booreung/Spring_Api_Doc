"""
    전체 모듈 파이프라인 구성
"""

from config import PROJECT_ROOT, CONTROLLER_ROOT, SERVICE_ROOT, DAO_ROOT, SQL_ROOT
from parser.api_spec_builder import build_api_spec
from generator.html_generator import generate_html
from generator.json_generator import generate_json
from generator.excel_generator import generate_excel
import subprocess

def main():

    # API 명세분석
    api_spec = build_api_spec(PROJECT_ROOT, PROJECT_ROOT, PROJECT_ROOT, PROJECT_ROOT) 
    #지금은 controller, service, dao, sql 이 한 루트 디렉토리 안에 있기 때문에 이렇게 세팅

    # Json 변환
    generate_json(api_spec, r"output\api_spec.json")

    # HTML 변환
    generate_html(r"output\api_spec.json", r"output\api_spec.html")

    # Excel 변환
    #generate_excel(r"output\api_spec.json", r"output\API명세서.xlsx")

    print("\n### API 명세 문서화 작업완료 ###")

    # app 실행
    subprocess.run(["python", r"dashboard\app.py"])


if __name__ == "__main__":
    main()