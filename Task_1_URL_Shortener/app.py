from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return "URL Shortener Backend is Running!"


@app.route("/api/health")
def health_check():
    return jsonify({
        "status": "success",
        "message": "Backend is healthy"
    })


if __name__ == "__main__":
    app.run(debug=True)