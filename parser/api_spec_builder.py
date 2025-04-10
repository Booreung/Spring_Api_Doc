"""
    Controller, Service, Dao, SQL parser에서 나온 결과값을 JSON으로 묶는 통합 빌더
"""

import os
from enum import Enum
from parser.controller_parser import parse_controller_file
from parser.service_parser import parse_service_file
from parser.dao_parser import parse_dao_file
from parser.sql_mapper_parser import parse_sql_mapper_file

class FileType(Enum):
    CONTROLLER = "controller"
    SERVICE = "service"
    DAO = "dao"
    SQL = "sql"


def build_api_spec(controller_dir, service_dir, dao_dir, sql_dir):
    api_spec = []

    # 1. 파일구분 및 파싱
    """
        프로젝트의 controller, service, dao, sql 파일들의 최상단 경로는 직접 넣어줘야함 
        why? : 전체를 긁어오면 분명 필요없는 데이터까지 올 수 있음
        스스로 파일 구조 자체는 인지하고 상단 폴더명의 경로만 가져오면 전부 읽히는 로직임
    """
    controller_data = parse_file_by_type(FileType.CONTROLLER, controller_dir)
    service_data = parse_file_by_type(FileType.SERVICE, service_dir)
    dao_data = parse_file_by_type(FileType.DAO, dao_dir)
    sql_data = parse_file_by_type(FileType.SQL, sql_dir)

    # 2. 연결 매핑
    for ctrl in controller_data:
        api_entry = {
            "controller_class" : ctrl["controller"],
            "url" : ctrl["full_url"],
            "http_method" : ctrl["method"],
            "controller_method" : ctrl["function"],
            "service_class" : None,
            "service_method" : None,
            "dao_class" : None,
            "dao_method" : None,
            "dao->sql_mapper_id" : None, 
            "params" : None,
            "sql_id" : None,
            "sql_type" : None,
            "Query" : None
        }

        # Controller -> Service
        for svc in service_data:
            if svc["method"] == ctrl["called_service_method"]:
                api_entry["service_class"] = svc["service"]
                api_entry["service_method"] =svc["method"]

                # Service -> Dao
                for dao in dao_data:
                    if dao["method"] == svc["called_dao_method"]:
                        api_entry["dao_class"] = dao["dao_class"]
                        api_entry["dao_method"] = dao["method"]
                        api_entry["dao->sql_mapper_id"] = dao["mapper_id"]
                        api_entry["params"] = dao["params"]

                        # Dao -> Service
                        for sql in sql_data:
                            if sql["sql_id"] == dao["method"]:
                                api_entry["sql_id"] = sql["sql_id"]
                                api_entry["sql_type"] = sql["sql_type"]
                                api_entry["Query"] = sql["Query"]

        api_spec.append(api_entry)

        if(api_spec):
            print("\n### 소스코드 파싱 완료 ###\n")
            print(f"### 총 API 수 : {len(api_spec)}\n")

    return api_spec

# 파일 구분
def parse_file_by_type(file_type : FileType, root_dir: str):
    parsed_data = []
    ext = ".xml" if file_type == FileType.SQL else ".java"
    count = 0

    for dirpath, _, filenames in os.walk(root_dir):
        for fname in filenames:
            if not fname.endswith(ext):
                continue

            full_path = os.path.join(dirpath, fname)

            if file_type == FileType.CONTROLLER:
                parsed_data += parse_controller_file(full_path)
        
            elif file_type == FileType.SERVICE:
                parsed_data += parse_service_file(full_path)

            elif file_type == FileType.DAO:
                parsed_data += parse_dao_file(full_path)
        
            elif file_type == FileType.SQL:
                parsed_data += parse_sql_mapper_file(full_path)

            count += 1

    print(f"### {file_type.value.upper()} 파일 {count}개 분석 완료")
        
    return parsed_data


# test
# if __name__ == "__main__":
#     spec = build_api_spec("sample", "sample", "sample", "sample")
#     import json
#     print(json.dumps(spec, indent=2, ensure_ascii=False))