# retrieves all of the technical indicators needed to determine buy and sell signals

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
            time.sleep(4)
            return response.json()
        else:
            time.sleep(4)
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

def get_price_of_one_crypto(symbol, interval):
    print ("Getting price of " + str(symbol) + "\n")
    url = 'https://api.taapi.io/price?'
    params = {
        'exchange': 'binance',
        'symbol': symbol,
        'interval': interval
    }

    response = make_api_get_request(url=url, params=params)
    response = response['value']
    return response



def get_rsi(symbol, exchange):
    print ("Getting RSI of " + str(symbol) + "\n")
    url = 'https://api.taapi.io/rsi?'
    params = {
        'exchange': exchange,
        'symbol': symbol,
        'interval': '1d',
    }

    response = make_api_get_request(url=url, params=params)
    if response:
        response = response['value']
        if response > 50.0:
            return 'long'
        else:
            return 'short'
    
    

def get_macd_signal(symbol, exchange):
    print ("Getting MACD of " + str(symbol) + "\n")
    url = 'https://api.taapi.io/macd?'
    params = {
        'exchange': exchange,
        'symbol': symbol,
        'interval': '1d',
    }
    response = make_api_get_request(url=url, params=params)

    if response:
        response = response['valueMACDHist']
        if response > 0.0:
            return 'long'
        else:
            return 'short'
    

def get_stoch(symbol, exchange):
    print ("Getting Stochastic of " + str(symbol) + "\n")
    url = 'https://api.taapi.io/stoch?'
    params = {
        'exchange': exchange,
        'symbol': symbol,
        'interval': '1d',
        'kPeriod': 14
    }
    response = make_api_get_request(url=url, params=params)
    if response:
        response = response['valueK']
        if response > 50.0:
            return 'long'
        else:
            return 'short'