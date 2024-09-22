import os
from flask import Flask, jsonify, request
import redis

app = Flask(__name__)

# Get Redis connection details from environment variables
REDIS_HOST = os.getenv("REDIS_HOST", "redis")
REDIS_PORT = int(os.getenv("REDIS_PORT", "6380"))

# Initialize Redis client
r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, db=0)


@app.route("/")
def home():
    return "Hello from Python API!\n"


@app.route("/set", methods=["POST"])
def set_key():
    data = request.get_json()
    key = data.get("key")
    value = data.get("value")
    if key and value:
        r.set(key, value)
        return jsonify({"message": f"Key '{key}' set to '{value}'."}), 200
    return jsonify({"error": "Please provide 'key' and 'value'."}), 400


@app.route("/get/<key>", methods=["GET"])
def get_key(key):
    value = r.get(key)
    if value:
        return jsonify({"key": key, "value": value.decode("utf-8")}), 200
    return jsonify({"error": f"Key '{key}' not found."}), 404


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
