# app.py
from flask import Flask, request, jsonify, render_template
import os
import redis
from bs4 import BeautifulSoup
from get_data import get_all_mf_data

# get the environment variables
REDIS_HOST = os.getenv("REDIS_HOST", "localhost")
REDIS_PORT = int(os.getenv("REDIS_PORT", 6379))
CACHE_EXPIRY = 3600  # 1 hour expiry time for cache
PORT = int(os.environ.get("DATA_SERVICE_PORT", 6000))

cache = redis.Redis(host=REDIS_HOST, port=REDIS_PORT)
# check if the redis server is running
app = Flask(__name__)


@app.route("/get_all_mfs", methods=["GET"])
def getData():

    key = "all_mf_data"
    data = cache.get(key)

    if data:
        return data

    try:
        data = get_all_mf_data()
        cache.setex(key, CACHE_EXPIRY, data)
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    # check if connected to redis
    try:
        cache.ping()
        print("Connected to Redis")
    except redis.ConnectionError:
        print("Error: Redis server not available")
        exit(1)
    print(f"Running on port {PORT}")
    app.run(host="0.0.0.0", port=PORT, debug=True)
