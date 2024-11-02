from flask import Flask, request, jsonify, render_template
import os
import redis
import json
from bs4 import BeautifulSoup
from get_data import get_all_mf_data, get_mfs_having, get_mf_data
from constants import *
from utils import cache_response

import logging
logging.basicConfig(level=logging.DEBUG)

cache = redis.Redis(host=REDIS_HOST, port=REDIS_PORT)
# check if the redis server is running
app = Flask(__name__)

@app.route("/get_all_mfs", methods=["GET"])
@cache_response(lambda *args, **kwargs: "all_mf_data", cache)
def get_data():
    return get_all_mf_data()

@app.route("/get_similar_mfs", methods=["GET"])
@cache_response(lambda *args, **kwargs: f"similar_mfs_{request.args.get('mf_string')}", cache)
def get_similar_mfs():
    mf_string = request.args.get("mf_string")
    if not mf_string:
        return jsonify({"error": "Please provide a mutual fund name"})
    return get_mfs_having(mf_string)

@app.route("/get_mf_data", methods=["GET"])
@cache_response(lambda *args, **kwargs: f"mf_data_{request.args.get('mf_id')}", cache)
def get_mf_data():
    mf_id = request.args.get("mf_id")
    if not mf_id:
        return jsonify({"error": "Please provide a mutual fund id"})
    return get_mf_data(mf_id)


if __name__ == "__main__":
    # check if connected to redis
    try:
        cache.ping()
        # print redis connection details
        # print(cache.connection_pool.connection_kwargs)
        # print("Connected to Redis")
        logging.info("Connected to Redis")
    except redis.ConnectionError:
        logging.error("Error: Redis server not available")
        exit(1)
    logging.info(f"Running on port {PORT}")
    app.run(host="0.0.0.0", port=PORT, debug=True)
