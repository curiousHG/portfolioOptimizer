import requests
from config import APIConfig
from mftool import Mftool
from utils import search_closest_keys
from data import mfMap
mf = Mftool()

def get_all_mf_data():
    response = mf.get_available_schemes("")
    return response

def get_mfs_having(mf_string):
    results = search_closest_keys(mf_string, mfMap) #results is a dictionary
    return results

def get_mf_data(mf_id):
    response = mf.get_scheme_quote(mf_id)
    return response