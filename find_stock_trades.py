from ta_api import *
from send_discord_message import *
import time
from update_txt_file import *
from get_stock_data import *


NYSE_symbols = []
NASDAQ_symbols = []

get_tech_indicators(NYSE_symbols, NASDAQ_symbols)