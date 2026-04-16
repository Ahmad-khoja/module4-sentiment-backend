from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import random
import psycopg2
from datetime import datetime

app = Flask(__name__)
CORS(app)

DEBUG_MODE = os.getenv("DEBUG", "False").lower() == "true"
HOST_IP = os.getenv("HOST_IP", "0.0.0.0")

DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT", "5432")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")

API_KEY = os.getenv("API_KEY", "secret123")


def get_db_connection():
    return psycopg2.connect(
        host=DB_HOST,
        port=DB_PORT,
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD
    )


@app.route("/")
def home():
    return jsonify({
        "message": "Sentiment Analysis Backend is running"
    })


@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()

    if not data or "text" not in data:
        return jsonify({"error": "Text is required"}), 400

    text = data["text"].strip()

    if text == "":
        return jsonify({"error": "Text cannot be empty"}), 400

    sentiment = random.choice(["positive", "neutral", "negative"])
    timestamp = datetime.utcnow()

    try:
        conn = get_db_connection()
        cur = conn.cursor()

        cur.execute(
            """
            INSERT INTO sentiment_results (text_input, sentiment_label, created_at)
            VALUES (%s, %s, %s)
            """,
            (text, sentiment, timestamp)
        )

        conn.commit()
        cur.close()
        conn.close()
    except Exception as e:
        return jsonify({"error": f"Database insert failed: {str(e)}"}), 500

    return jsonify({
        "text": text,
        "sentiment": sentiment,
        "timestamp": timestamp.isoformat()
    })

#This is new
@app.route("/results", methods=["GET"])
def results():
    api_key = request.args.get("api_key")

    if api_key != API_KEY:
        return jsonify({"error": "Unauthorized"}), 401

    try:
        conn = get_db_connection()
        cur = conn.cursor()

        cur.execute("""
            SELECT id, text_input, sentiment_label, created_at
            FROM sentiment_results
            ORDER BY created_at DESC
        """)

        rows = cur.fetchall()

        results_list = []
        for row in rows:
            results_list.append({
                "id": row[0],
                "text_input": row[1],
                "sentiment_label": row[2],
                "created_at": row[3].isoformat() if row[3] else None
            })

        cur.close()
        conn.close()

        return jsonify(results_list)

    except Exception as e:
        return jsonify({"error": f"Database read failed: {str(e)}"}), 500


if __name__ == "__main__":
    app.run(debug=DEBUG_MODE, host=HOST_IP, port=5000)