from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/feishu_plugin", methods=["POST"])
def handle_feishu():
    data = request.get_json()

    # 处理 challenge 验证
    if "challenge" in data:
        return jsonify({"challenge": data["challenge"]})

    # 其他插件逻辑可以写在这里
    print("飞书插件接收到数据:", data)

    return jsonify({"code": 0, "message": "处理成功"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
