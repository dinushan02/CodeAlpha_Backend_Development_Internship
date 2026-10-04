from flask import Flask, jsonify, request

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


@app.route("/api/shorten", methods=["POST"])
def shorten_url():
    data = request.get_json()

    if not data or not data.get("url"):
        return jsonify({
            "status": "error",
            "message": "URL is required"
        }), 400

    return jsonify({
        "status": "success",
        "message": "URL received successfully",
        "url": data.get("url")
    })


if __name__ == "__main__":
    app.run(debug=True)