from flask import Flask, jsonify, request, redirect
from secrets import token_hex
import sqlite3

app = Flask(__name__)


def init_db():
    connection = sqlite3.connect("url_shortener.db")

    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS urls (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            short_code TEXT UNIQUE NOT NULL,
            original_url TEXT NOT NULL
        )
    """)

    connection.commit()
    connection.close()


def save_url(short_code, original_url):
    connection = sqlite3.connect("url_shortener.db")

    cursor = connection.cursor()

    cursor.execute(
        "INSERT INTO urls (short_code, original_url) VALUES (?, ?)",
        (short_code, original_url)
    )

    connection.commit()
    connection.close()


def short_code_exists(short_code):
    connection = sqlite3.connect("url_shortener.db")

    cursor = connection.cursor()

    cursor.execute(
        "SELECT 1 FROM urls WHERE short_code = ?",
        (short_code,)
    )

    result = cursor.fetchone()

    connection.close()

    return result is not None


def get_original_url(short_code):
    connection = sqlite3.connect("url_shortener.db")

    cursor = connection.cursor()

    cursor.execute(
        "SELECT original_url FROM urls WHERE short_code = ?",
        (short_code,)
    )

    result = cursor.fetchone()

    connection.close()

    if result:
        return result[0]

    return None


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

    original_url = data.get("url")
    short_code = token_hex(3)

    while short_code_exists(short_code):
        short_code = token_hex(3)

    save_url(short_code, original_url)

    short_url = f"http://127.0.0.1:5000/{short_code}"

    return jsonify({
        "status": "success",
        "original_url": original_url,
        "short_code": short_code,
        "short_url": short_url
    })


@app.route("/<short_code>")
def redirect_to_original(short_code):
    original_url = get_original_url(short_code)

    if original_url:
        return redirect(original_url)

    return jsonify({
        "status": "error",
        "message": "Short URL not found"
    }), 404


if __name__ == "__main__":
    init_db()
    app.run(debug=True)