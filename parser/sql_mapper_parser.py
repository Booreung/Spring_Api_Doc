"""
    SQL XML 파일을 파싱하여 API 명세 리스트를 반환
"""

import re
import os
from typing import List, Dict


def parse_sql_mapper_file(file_path : str) -> List[Dict]:
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    result = []

    # 쿼리 추출
    pattern = re.compile(r'<(select|insert|update|delete)\s+id="([^"]+)"[^>]*?>\s*<!\[CDATA\[(.*?)\]\]>', re.DOTALL)

    for match in pattern.finditer(content):
        sql_type = match.group(1)
        sql_id = match.group(2)
        sql_query = match.group(3).strip()

        result.append({
            "mapper_file" : os.path.basename(file_path),
            "sql_id" : sql_id,
            "sql_type" : sql_type,
            "Query" : sql_query
        })

    return result

    # 클로저(호이스팅 +), 역순버그 JS(문제점)
    # 튜플 ->  속도가 빠르고 변화가 없음(데이터 자체의 무결성 보장)

# 예시
# if __name__ ==  "__main__":
#     test_file = r"sample\sampleSQL.xml"  # SQL 파일 위치경로를 입력할것
#     if os.path.exists(test_file):
#         import json
#         parsed = parse_sql_mapper_file(test_file)
#         print(json.dumps(parsed, indent=2, ensure_ascii=False))
#     else:
#         print("### 샘플 SQL Mapper 파일이 존재하지 않습니다.")

