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
    requests json data and returns all data to sort_data().
    """
    data  = requests.get(url)
    data = data.json()
    sort_data(data)

def sort_data(input_request):
    """
    User can request specific parts of the json data like price, or all here.
    Uses a while loop so data reloading wont be needed.
    """
    while True:
        print("Type 'help' for more info")
        sort = input(": ")
        if sort == 'all':
            print(input_request)
        elif sort == 'help':
            print("Enter 'quit' to exit\n'restart' to restart")
            print("'all' : dumps all info.\n'price' : shows current share price")
        elif sort == 'price':
            print(input_request[0]['price'])
        elif sort == 'quit':
            quit()
        elif sort == 'restart':
            get_data()
        else:
            print("Data not found, try again")
            continue
        


get_data()
