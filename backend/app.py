from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import random

app = Flask(__name__)
CORS(app)

DEBUG_MODE = os.getenv("DEBUG", "False").lower() == "true"
HOST_IP = os.getenv("HOST_IP", "0.0.0.0")

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

    result = random.choice(["positive", "neutral", "negative"])

    return jsonify({
        "text": text,
        "sentiment": result
    })

if __name__ == "__main__":
    app.run(debug=DEBUG_MODE, host=HOST_IP, port=5000)