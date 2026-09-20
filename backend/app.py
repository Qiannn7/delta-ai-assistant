from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/api/hello",methods=["GET"])
def hello():
    return jsonify({"msg":"hello delta ai assistant","code":200})

#对话接口，POST请求，接收用户question
@app.route("/api/chat",methods=["POST"])
def chat():
    data = request.get_json()
    question = data.get("question","")
    #模拟AI回复，后面替换成真实大模型
    reply = f"AI回复：收到你的问题【{question}】"
    return jsonify({"code":200,"reply":reply})

if __name__ == "__main__":
    app.run(host="127.0.0.1",port=5000,debug=True)
