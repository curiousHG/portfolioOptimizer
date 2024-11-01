import requests
from config import APIConfig

def get_all_mf_data():
    url = f"{APIConfig.MF_DATA_API_URL}mf"
    response = requests.get(url)
    return response.json()