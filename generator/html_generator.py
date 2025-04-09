"""
    Json으로 변환된 api명세를 HTML로 변환
"""

import json
import os

def generate_html(json_path: str, output_path: str):
    with open(json_path, "r", encoding="utf-8") as f:
        api_spec = json.load(f)

    html = """
    <html>
    <head>
        <meta charset="utf-8">
        <title>Spring API 명세서</title>
        <style>
            body { font-family: 'Malgun Gothic', sans-serif; }
            table { border-collapse: collapse; width: 100%; }
            th, td { border: 1px solid #ccc; padding: 8px; font-size: 13px; }
            th { background-color: #f2f2f2; }
            pre { white-space: pre-wrap; word-wrap: break-word; font-family: 'Consolas', monospace; }
        </style>
    </head>
    <body>
    <h2>📘 Spring API 명세서</h2>
    <table>
        <tr>
            <th>URL</th><th>HTTP Method</th><th>Controller</th><th>Service</th>
            <th>DAO</th><th>SQL ID</th><th>SQL Type</th><th>Query</th>
        </tr>
    """

    for api in api_spec:
        html += f"""
        <tr>
            <td>{api.get('url', '-')}</td>
            <td>{api.get('http_method', '-')}</td>
            <td>{api.get('controller_method', '-')}</td>
            <td>{api.get('service_method', '-')}</td>
            <td>{api.get('dao_method', '-')}</td>
            <td>{api.get('sql_id', '-')}</td>
            <td>{api.get('sql_type', '-')}</td>
            <td><pre>{api.get('Query', '-')}</pre></td>
        </tr>
        """

    html += """
    </table>
    </body>
    </html>
    """

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(html)

    print(f"### HTML 명세서 저장 완료 → {output_path}")


if __name__ == "__main__":
    generate_html("output/api_spec.json", "output/api_spec.html")
    
