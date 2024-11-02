import os

FETCHING_DATA_FROM_CACHE = "Fetching data from cache"
FETCHING_DATA_FROM_API = "Fetching data from API"
DATA_CACHED = "Data cached"

# get the environment variables
REDIS_HOST = os.getenv("REDIS_HOST", "localhost")
REDIS_PORT = int(os.getenv("REDIS_PORT", 6379))
CACHE_EXPIRY = 3600  # 1 hour expiry time for cache
PORT = int(os.environ.get("DATA_SERVICE_PORT", 6000))