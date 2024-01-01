from ta_api import make_api_get_request
from get_api_key import get_env_variable


env_variable_name = "API_KEY"
api_key = get_env_variable(env_variable_name)

indicator = "supertrend"

api_url = "https://api.taapi.io/" + indicator

params = {
    'secret': api_key,
    'exchange': 'binance',
    'symbol': 'BTC/USDT',
    'interval': '1h'
}

response_data = make_api_get_request(api_url, params=params)

print(response_data)