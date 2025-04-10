"""
    Java Service 파일을 파싱하여 API 명세 리스트를 반환
"""

import re
import os
from typing import List, Dict


def parse_service_file(file_path : str) -> List[Dict]:
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

        # 함수 정의 찾기
        method_match = re.search(r'(public|private|protected)\s+[\w<>]+\s+(\w+)\s*\(', line)
        if method_match:
            method_name = method_match.group(2)

            # DAO 호출 찾기
            dao_call = "" 
            for j in range(i+1, min(i+10, len(lines))):
                dao_match = re.search(r'(\w+)\.([a-zA-Z0-9_]+)\(', lines[j])
                if dao_match:
                    dao_call = dao_match.group(2)
                    break

            result.append({
                "service" : class_name,
                "method" : method_name,
                "called_dao_method" : dao_call
            })

    return result

# 예시
# if __name__ == "__main__":
#     test_file = r"sample\UserService.java"  # Service 파일 경로를 입력할것 or ServiceImpl 경로
#     if os.path.exists(test_file):
#         import json
#         parsed = parse_service_file(test_file)
#         print(json.dumps(parsed, indent=2, ensure_ascii=False))
#     else:
#         print("### 샘플 서비스 파일이 존재하지 않습니다.")