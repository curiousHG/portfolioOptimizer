from fuzzywuzzy import process, fuzz
import logging, json
from flask import jsonify
from constants import *
from functools import wraps
import redis



def search_closest_keys(query, data, limit=10):
    # Extract keys from data
    keys = list(data.keys())
    # Find closest matches to the query
    matches = process.extract(query, keys, scorer=fuzz.partial_ratio, limit=limit)
    # Get key-value pairs for the closest matches
    return {key: data[key] for key, score in matches if score > 50}  # Adjust score threshold if needed


# a wrapper function which checks in redis cache if present else returns data from api

def cache_response(cache_key_func: str , cache:redis.Redis, expiry=CACHE_EXPIRY):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            key = cache_key_func(*args, **kwargs)
            data = cache.get(key)
            
            if data:
                logging.info("FETCHING_DATA_FROM_CACHE")
                return data

            logging.info("FETCHING_DATA_FROM_API")
            try:
                data = func(*args, **kwargs)
                cache_data = json.dumps(data)
                cache.setex(key, expiry, cache_data)
                logging.info("DATA_CACHED")
                return data
            except Exception as e:
                return jsonify({"error": str(e)}), 500

        return wrapper
    return decorator