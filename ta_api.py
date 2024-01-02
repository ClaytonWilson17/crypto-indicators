# retrieves all of the technical indicators needed to determine buy and sell signals


import itertools
import csv
import pandas as pd
import requests
import time
from get_api_key import get_env_variable



def make_api_get_request(url, params=None):
    """
    Make a GET request to the specified API.

    Parameters:
    - url (str): The API endpoint URL.
    - symbol (str): The crypto symbol (example - ETH)
    - interval (str): Example - 1h
    - params (dict, optional): Query parameters to include in the request.
    - headers (dict, optional): Headers to include in the request.

    Returns:
    - dict: JSON response from the API.
    """

    env_variable_name = "API_KEY"
    api_key = {
        'secret': get_env_variable(env_variable_name)
    }

    api_key.update(params)

    try:
        response = requests.get(url, params=api_key)

        if response.status_code == 200:
            time.sleep(16)
            return response.json()
        else:
            time.sleep(16)
            response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error making API request: {e}")


def get_all_binance_symbols():
    print ("Getting all binance sybols\n")
    url = 'https://api.taapi.io/exchange-symbols?'
    params = {
        'exchange': 'binance'
    }

    response = make_api_get_request(url=url, params=params)
    return response

def get_price_of_one_crypto(symbol):
    print ("Getting price of " + str(symbol) + "\n")
    url = 'https://api.taapi.io/price?'
    params = {
    'exchange': 'binance',
    'symbol': symbol,
    'interval': '1h',
}

    response = make_api_get_request(url=url, params=params)
    response = response['value']
    return response


def get_supertrend(symbol):
    print ("Getting supertrend of " + str(symbol) + "\n")
    url = 'https://api.taapi.io/supertrend?'
    params = {
        'exchange': 'binance',
        'symbol': symbol,
        'interval': '15m',
        'period': 10,
        'multiplier': 3
    }

    response = make_api_get_request(url=url, params=params)
    return response