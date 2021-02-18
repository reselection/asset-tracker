#!/bin/python3

import pandas as pd
import json
from urllib.request import urlopen
import requests

asset = input("Enter asset ticker: ")

def asset_request(url):
    """
    requests json data
    """
    company_data  = requests.get(url)
    company_data = company_data.json()
    price = float(f"{company_data[0]['price']}")
    return price

url = (f"https://financialmodelingprep.com/api/v3/quote/{asset.upper()}?apikey=2bdce558ad8fcab19ca4cbd5abf8a21b")

print(asset_request(url))


