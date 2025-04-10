"""
    api_spec_builder.py 에서의 결과값을 api_spec.json으로 변환
"""

import json
from typing import List, Dict
from parser.api_spec_builder import build_api_spec

def generate_json(api_spec : List[Dict], output_path : str) -> None:
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(api_spec, f, indent=2, ensure_ascii=False)
        print(f"### Json 명세 저장 완료 -> {output_path}")


# test
# if __name__ == "__main__":
#     api_spec = build_api_spec("sample", "sample", "sample", "sample")
#     generate_json(api_spec, r"output\api_spec.json")

# 테스트 실행 명령어 python -m generator.json_generator