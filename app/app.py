from flask import Flask, jsonify

app = Flask(__name__)

@app.get("/health")
def health():
    return jsonify(status="ok")

@app.get("/")
def home():
    return jsonify(service="python-agri-devops-platform", version="0.1")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
