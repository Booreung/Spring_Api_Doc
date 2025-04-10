"""
    Controller, Service, Dao, SQL parser에서 나온 결과값을 JSON으로 묶는 통합 빌더
"""

import os
from parser.controller_parser import parse_controller_file
from parser.service_parser import parse_service_file
from parser.dao_parser import parse_dao_file
from parser.sql_mapper_parser import parse_sql_mapper_file


def build_api_spec(controller_dir, service_dir, dao_dir, sql_dir):
    api_spec = []

    # 1. 파일구분 및 파싱
    """
        프로젝트의 controller, service, dao, sql 파일들의 최상단 경로는 직접 넣어줘야함 
        why? : 전체를 긁어오면 분명 필요없는 데이터까지 올 수 있음
        스스로 파일 구조 자체는 인지하고 상단 폴더명의 경로만 가져오면 전부 읽히는 로직임
    """
    controller_data = parse_file_by_type("controller", controller_dir)
    service_data = parse_file_by_type("service", service_dir)
    dao_data = parse_file_by_type("dao", dao_dir)
    sql_data = parse_file_by_type("sql", sql_dir)

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
            print("### 소스코드 파싱 완료 ###\n")

    return api_spec

# 파일 구분
def parse_file_by_type(file_type, dir_path):
    parsed_data = []

    for fname in os.listdir(dir_path):
        if not fname.endswith(".java") and file_type != 'sql':
            continue
        if not fname.endswith(".xml") and file_type == "sql":
            continue

        full_path = os.path.join(dir_path, fname)

        if file_type == "controller":
            parsed_data += parse_controller_file(full_path)
        
        elif file_type == "service":
            parsed_data += parse_service_file(full_path)

        elif file_type == "dao":
            parsed_data += parse_dao_file(full_path)
        
        elif file_type == "sql":
            parsed_data += parse_sql_mapper_file(full_path)
        
    return parsed_data


# test
# if __name__ == "__main__":
#     spec = build_api_spec("sample", "sample", "sample", "sample")
#     import json
#     print(json.dumps(spec, indent=2, ensure_ascii=False))