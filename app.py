from flask import Flask, jsonify
from flask_cors import CORS  # Flask-CORS 추가

app = Flask(__name__)
CORS(app)  # 모든 도메인 허용

# 특정 도메인만 허용하려면 다음처럼 지정합니다.
# CORS(app, origins=["https://your-allowed-domain.com"])

@app.route('/api', methods=['GET'])
def api():
    response_data = {
        "message": "Hello, World!",
        "status": "success",
        "data": {
            "example_key": "example_value"
        }
    }
    return jsonify(response_data)

if __name__ == '__main__':
    app.run(debug=True)
