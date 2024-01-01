# retrieves all of the technical indicators needed to determine buy and sell signals


import itertools
import csv
import pandas as pd
import requests


def make_api_get_request(url, params=None, headers=None):
    """
    Make a GET request to the specified API.

    Parameters:
    - url (str): The API endpoint URL.
    - params (dict, optional): Query parameters to include in the request.
    - headers (dict, optional): Headers to include in the request.

    Returns:
    - dict: JSON response from the API.
    """
    try:
        response = requests.get(url, params=params, headers=headers)

        if response.status_code == 200:
            return response.json()
        else:
            response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error making API request: {e}")

# Example usage:
api_url = "https://jsonplaceholder.typicode.com/todos/1"
response_data = make_api_get_request(api_url)

print(response_data)
