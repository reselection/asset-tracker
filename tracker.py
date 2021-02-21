#!/bin/python3

import json
import requests
import time
from urllib.request import urlopen

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
    elif reqdata == 'quote':
        url = f"https://financialmodelingprep.com/api/v3/quote/{ticker.upper()}?apikey=2bdce558ad8fcab19ca4cbd5abf8a21b"
        asset_request(url)
    else:
        print("Enter 'quote' or 'profile'\nReturning...")
        time.sleep(3)
        get_data()

def asset_request(url):
    print("requesting data...")
    """
    requests json data and returns all data.
    """
    company_data  = requests.get(url)
    company_data = company_data.json()
    #price = f"{company_data[0]['price']}"
    data = f"{company_data}"
    sort_data(data)
    print(data)

def sort_data(input_request):
    pass    


get_data()
