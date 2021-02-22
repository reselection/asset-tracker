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
         asset_request_profile(url)
    elif reqdata == 'quote':
        url = f"https://financialmodelingprep.com/api/v3/quote/{ticker.upper()}?apikey=2bdce558ad8fcab19ca4cbd5abf8a21b"
        asset_request_quote(url)
    else:
        print("Enter 'quote' or 'profile'\nReturning...")
        time.sleep(3)
        get_data()

def asset_request_quote(url):
    """
    requests quote data in json format and returns it to sort_data_quote
    """
    data = requests.get(url)
    if not data.json():
        print("Could't reach URL, check spelling and try again")
        get_data()
    data = data.json()
    sort_data_quote(data)

def sort_data_quote(input_request):
    """User can filter quote data here and view options"""
    quote_json = ['all','price','changePercentage','change','dayHigh','dayLow','yearHigh','yearLow','marketCap','priceAvg50',
    'priceAvg200', 'volume','open','previousClose','earningsAnnouncement','sharesOutstanding']
    while True:
        print("Type 'help' for more info")
        sort = input(": ")
        if sort == "all":
            print(input_request)
        elif sort == 'help':
            print("Type 'quit to exit\n'restart' to restart")
            print("Options:")
            for x in quote_json:
                print(f"\t- {x}")
        elif sort == 'restart':
            get_data()
        elif sort == 'quit':
            break
        elif sort:
            for x in quote_json:
                if sort.lower() == x.lower():
                    print(input_request[0][x])
                    continue
        else:
            print("Data not found, try again")
            continue
 

def asset_request_profile(url):
    print("requesting data...")
    """
    requests json data and returns all data to sort_data_profile().
    """
    data  = requests.get(url)
    data = data.json()
    sort_data_profile(data)

def sort_data_profile(input_request):
    """
    User can request specific parts of the json data like price, or all here.
    Uses a while loop so data reloading wont be needed.
    """
    profile_json = ['all','price','volAvg','mktCap','website','description','industry','ceo','sector','fullTimeEmployees']

    while True:
        print("Type 'help' for more info")
        sort = input(": ")
        if sort == 'all':
            print(input_request)
        elif sort == 'help':
            print("Enter 'quit' to exit\n'restart' to restart")
            print("Options:")
            for x in profile_json:
                print(f"\t- {x}")
        elif sort == 'restart':
            get_data()
        elif sort == 'quit':
            break
        elif sort:
            for x in profile_json:
                if sort.lower() == x.lower():
                    print(input_request[0][x])
                    continue
        else:
            print("Data not found, try again")
            continue
        


get_data()
