from flask import Flask, jsonify

app = Flask(__name__)

@app.get("/")
def home():
    return jsonify(
        message="Hello from Python, Harness CI and Docker Hub!",
        version="1.0.0"
    )

@app.get("/health")
def health():
    return jsonify(status="healthy")

@app.get("/info")
def info():
    return jsonify(
        application="python-harness-ci-demo",
        language="Python",
        framework="Flask"
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
