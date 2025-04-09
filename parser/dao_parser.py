"""
    Java DAO 파일을 파싱하여 API 명세 리스트를 반환
"""

import re
import os
from typing import List, Dict

def parse_dao_file(file_path : str) -> List[Dict]:
    with open(file_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    result = []
    class_name = ""
    current_method = {}

    for i, line in enumerate(lines):
        line = line.strip()

        # 클래스명 추출
        class_match = re.search(r'class\s+(\w+)\s*\{?', line)
        if class_match:
            class_name = class_match.group(1)

        # 메소드명 추출
        fn_match = re.search(r'(public|private|protected)\s+[\w<>]+\s+(\w+)\s*\(', line)
        if fn_match:
            function_name = fn_match.group(2)

        # C,R,U,D 구분 추출
        method_match = re.search(r'(select|insert|update|delete|listScroll|list)\("([\w\.]+)"\s*,\s*(\w+)\)', line)
        if method_match:
            operation = method_match.group(1)
            mapper_id = method_match.group(2)
            params = method_match.group(3)

            result.append({
                "dao_class" : class_name,
                "method" : function_name,
                "operation" : operation,
                "mapper_id" : mapper_id,
                "params" : params 
            })

    return result

# 예시
if __name__ == "__main__":
    test_file = r"sample\UserDao.java"  # Dao 파일 경로를 입력할 것
    if os.path.exists(test_file):
        import json
        parsed = parse_dao_file(test_file)
        print(json.dumps(parsed, indent=2, ensure_ascii=False))
    else:
        print("### 샘플 Dao 파일이 존재하지 않습니다.")