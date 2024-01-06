from ta_api import *
import time
from send_discord_message import *

start_time = time.time()

res = get_price_of_one_crypto('BTC/USDT', '1d')

print (res)

#print("Elapsed time: ", time.time() - start_time)
