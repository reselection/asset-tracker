#!/bin/python3

import json
from urllib.request import urlopen
import requests


def get_data():
    """
    Asks user for all the data it requires, then sends it to asset_request.
    """
    print("Press 'quit' to exit")
    ticker = input("Enter asset ticker: ")
    if ticker == 'quit':
        quit()
    reqdata = input("Recieve quote or profile?: ")
    if reqdata == 'quit':
        quit()
    elif reqdata == 'profile':
         url = f"https://financialmodelingprep.com/api/v3/profile/{ticker.upper()}?apikey=2bdce558ad8fcab19ca4cbd5abf8a21b"
         asset_request(url)

def asset_request(url):
    print("requesting data...")
    """requests json data and returns the price"""
    company_data  = requests.get(url)
    company_data = company_data.json()
    #price = f"{company_data[0]['price']}"
    price = f"{company_data}"
    print(float(price))

def sort_data(input_request):
    pass


get_data()
