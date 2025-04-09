"""
    Java Controller 파일을 파싱하여 API 명세 리스트를 반환
"""

import re
import os
from typing import List, Dict


def parse_controller_file(file_path : str) -> List[Dict]:
    with open(file_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    result = []
    class_name = ""
    base_url = ""
    current_method = {}

    for i, line in enumerate(lines):
        line = line.strip()

        # 클래스명 추출
        class_match = re.search(r'class\s+(\w+)\s*\{?', line)
        if class_match:
            class_name = class_match.group(1)

        # 클래스 레벨 RequestMapping(Optional) -> @Controller 만 사용하는 경우도 고려
        base_match = re.search(r'@RequestMapping\("(.*?)"\)', line)
        if base_match:
            base_url = base_match.group(1)
        else:
            base_url = ""

        # 메서드의 요청 방법 추출 RequestMapping / GetMapping / PostMapping
        http_match = re.search(r'@(GetMapping|PostMapping|PutMapping|DeleteMapping|RequestMapping)\s*(\(([^)]*)\))?', line)
        if http_match:
            method_type = http_match.group(1).replace('Mapping', '').upper()
            sub_url = http_match.group(3) or ""

            # 함수명 추출
            func_line = lines[i+1].strip() if i+1 < len(lines) else ""
            func_match = re.search(r'(public|private|protected)\s+[\w<>]+\s+(\w+)\s*\(', func_line)
            function_name = func_match.group(2) if func_match else ""

            # service 호출 메소드 찾기
            service_call = ""
            for j in range(i+1, min(i+10, len(lines))):
                service_match = re.search(r'(\w+)\.([a-zA-Z0-9_]+)\(', lines[j])
                if service_match:
                    service_call = service_match.group(2)
                    break

            # 결과값
            result.append({
                "controller": class_name,
                "base_url": base_url,
                "method": method_type,
                "full_url": base_url + sub_url,
                "function": function_name,
                "called_service_method": service_call
            })

    return result

# 예시 실행
if __name__== "__main__":
    test_file = r"sample\UserController.java"
    if os.path.exists(test_file):
        import json
        parsed = parse_controller_file(test_file)
        print(json.dumps(parsed, indent=2, ensure_ascii=False))
    else:
        print(" ### 샘플 컨트롤러 파일이 존재하지 않습니다.")