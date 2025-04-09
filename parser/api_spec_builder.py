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

    # 1. 파싱
    controller_data = []
    service_data = []
    dao_data = []
    sql_data = []

    # Controller
    for fname in os.listdir(controller_dir):
        if fname.endswith(".java"):
            controller_data += parse_controller_file(os.path.join(controller_dir, fname))

    # Service
    for fname in os.listdir(service_dir):
        if fname.endswith(".java"):
            service_data += parse_service_file(os.path.join(service_dir, fname))

    # Dao
    for fname in os.listdir(dao_dir):
        if fname.endswith(".java"):
            dao_data += parse_dao_file(os.path.join(dao_dir, fname))

    # SQL
    for fname in os.listdir(sql_dir):
        if fname.endswith(".xml"):
            sql_data += parse_sql_mapper_file(os.path.join(sql_dir, fname))

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
            "dao->sql mapper_id" : None, 
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
                        api_entry["dao->sql mapper_id"] = dao["mapper_id"]
                        api_entry["params"] = dao["params"]

                        # Dao -> Service
                        for sql in sql_data:
                            if sql["sql_id"] == dao["method"]:
                                api_entry["sql_id"] = sql["sql_id"]
                                api_entry["sql_type"] = sql["sql_type"]
                                api_entry["Query"] = sql["Query"]

        api_spec.append(api_entry)

    return api_spec


# test
if __name__ == "__main__":
    spec = build_api_spec("sample", "sample", "sample", "sample")
    import json
    print(json.dumps(spec, indent=2, ensure_ascii=False))