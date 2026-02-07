from flask import Flask, Response, request
from prometheus_client import Counter, Histogram, generate_latest, CONTENT_TYPE_LATEST

app = Flask(__name__)

# Метрики
HTTP_REQUESTS = Counter(
    "http_requests_total",
    "Total HTTP requests",
    ["method", "path", "status"]
)

HTTP_LATENCY = Histogram(
    "http_request_duration_seconds",
    "HTTP request latency",
    ["method", "path"]
)

@app.before_request
def before():
    request._timer = HTTP_LATENCY.labels(request.method, request.path).time()
    request._timer.__enter__()

@app.after_request
def after(response):
    HTTP_REQUESTS.labels(
        request.method,
        request.path,
        str(response.status_code)
    ).inc()
    return response

@app.teardown_request
def teardown(exc):
    if hasattr(request, "_timer"):
        request._timer.__exit__(None, None, None)

@app.route("/")
def home():
    return "Agri Digital Platform is running!"

@app.route("/metrics")
def metrics():
    return Response(
        generate_latest(),
        mimetype=CONTENT_TYPE_LATEST
    )

# 🔥 ВОТ ЭТО БЫЛО ОТСУТСТВУЮЩЕЕ
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
