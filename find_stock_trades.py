from ta_api import *
from send_discord_message import *
import time
from update_txt_file import *
from get_stock_data import *

def determine_signal(stock):
    print ("Getting signal for: " + str(stock['Symbol']))
    if stock['RSI'] > float(50):
        if stock['MACD_line'] > stock['MACD_signal']:
            if stock['Stochastic'] > float(50):
                return ('long')
    return None


NYSE_symbols = ['L', 'HD']
NASDAQ_symbols = ['MSFT', 'AAPL', 'AMD', 'NVDA']

stocks = get_tech_indicators(NYSE_symbols, NASDAQ_symbols)

stocks_to_long = []

for stock in stocks:
    try:
        signal = determine_signal(stock)
        if signal == 'long':
            stocks_to_long.append(stock['Symbol'])
    except:
        None






