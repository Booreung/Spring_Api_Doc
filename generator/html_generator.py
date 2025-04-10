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
            pre.query { white-space: pre-wrap; word-wrap: break-word; font-family: 'Consolas', monospace; max-height: 300px; overflow: auto; }
            td.bold-col { font-weight: bold;}
            .btn_back{
                 display: flex;
                 width: 100px;
                 height: 30px;
                 text-align: center;
                 text-decoration: none;
                 justify-content: center;
                 border: 1px solid #D9D9D9;
                 padding: 15px;
                 margin-bottom: 10px;
                 border-radius: 15px;
                 background-color: black;
                 color: #D9D9D9;
                 font-weight: bold;
                 font-size: larger;
             }
        </style>
    </head>
    <body>
    <h2>📘 Spring API 명세서</h2>
    <div><a href="/" class="btn_back">돌아가기</a></div>
    <hr>
    <table>
        <tr>
            <th>URL</th><th>HTTP Method</th><th>Controller</th><th>Service</th>
            <th>DAO</th><th>SQL ID</th><th>SQL Type</th><th>Params</th><th>Query</th>
        </tr>
    """

    for api in api_spec:
        html += f"""
        <tr>
            <td class="bold-col">{api.get('url', '-')}</td>
            <td class="bold-col">{api.get('http_method', '-')}</td>
            <td class="bold-col">{api.get('controller_method', '-')}</td>
            <td class="bold-col">{api.get('service_method', '-')}</td>
            <td class="bold-col">{api.get('dao_method', '-')}</td>
            <td class="bold-col">{api.get('sql_id', '-')}</td>
            <td class="bold-col">{api.get('sql_type', '-')}</td>
            <td class="bold-col">{api.get('params', '-')}</td>
            <td>
                <button onclick="toggleQuery(this)">보기</button>
                <pre class="query" style="display:none;">{api.get('Query', '-')}</pre>
            </td>
        </tr>
        """

    html += """
    </table>
    <script>
        function toggleQuery(button) {
            const queryElement = button.nextElementSibling;
            if (queryElement.style.display === "none") {
                queryElement.style.display = "block";
                button.innerText = "숨기기";
            } else {
                queryElement.style.display = "none";
                button.innerText = "보기";
            }
        }
    </script>
    </body>
    </html>
    """

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(html)

    print(f"### HTML 명세서 저장 완료 → {output_path}")


# if __name__ == "__main__":
#     generate_html(r"output/api_spec.json", r"output/api_spec.html")
    
