# retrieves all of the technical indicators needed to determine buy and sell signals


import itertools
import csv
import pandas as pd
import requests
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
    try:
        response = requests.get(url, params=params)

        if response.status_code == 200:
            return response.json()
        else:
            response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error making API request: {e}")






