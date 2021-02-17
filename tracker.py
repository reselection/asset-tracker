#!/bin/python3

import requests
import pandas as pd

api = '2bdce558ad8fcab19ca4cbd5abf8a21b'
search = input('Enter a stock or crypto: ')
url = f'https://financialmodelingprep.com/api/v3/profile/{search}?apikey={api}'

print(url)
