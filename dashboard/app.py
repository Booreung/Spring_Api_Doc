"""
    미리 만들어지 api_spec.html을 통해 Flask로 웹 대시보드 띄우기 => localhost:5000
"""

from flask import Flask, render_template
import os

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HTML_PATH = os.path.join(BASE_DIR, "output", "api_spec.html")

@app.route("/")
def home():
    return "<h2>Spring API 문서 자동화 대시보드 🎯</h2><p><a href='/api-doc'>API 명세 보기</a></p>"

@app.route("/api-doc")
def api_doc():
    if not os.path.exists(HTML_PATH):
        print("### 명세서 파일이 존재하지 않습니다. 먼저 HTML을 생성해주세요.")
        return "<h3>명세서 파일이 존재하지 않습니다. 먼저 HTML을 생성해주세요.</h3>"
    
    with open(HTML_PATH, "r", encoding="utf-8") as f:
        html_content = f.read()
    return html_content


# 테스트
if __name__ == "__main__":
    app.run(debug=True)