from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

#测试接口
@app.route("/api/hello",methods=["GET"])
def hello():
    return jsonify({"msg":"hello delta ai assistant","code":200})

if __name__ == "__main__":
    app.run(host="127.0.0.1",port=5000,debug=True)
