from flask import Flask, render_template, jsonify
import requests
import os

app = Flask(__name__)

BACKEND_URL = os.getenv("BACKEND_URL", "http://localhost:5000")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/api/weather/<city>")
def get_weather(city):
    response = requests.get(f"{BACKEND_URL}/weather/{city}")
    return jsonify(response.json()), response.status_code

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)