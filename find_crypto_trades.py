from ta_api import *
from send_discord_message import *
import time
from update_txt_file import *
start_time = time.time()


symbols = get_all_binance_symbols()

all_binance_symbols = []
for sym in symbols:
    try:
        if '/USDT' in sym:
            # price is not needed for now. We can add price restrictions later
            # price = get_price_of_one_crypto(sym)
            all_binance_symbols.append(sym)
    except:
        None

#all_binance_symbols = all_binance_symbols[0:10]

cryptos_to_trade = []
for sym in all_binance_symbols:
    if 'long' == get_macd_signal(sym, "binance"):
        if 'long' == get_rsi(sym, "binance"):
            if 'long' == get_stoch(sym, "binance"):
                print ('Adding ' + str(sym) + ' to list \n')
                cryptos_to_trade.append(sym)


file_path = 'coins_with_long_signal.txt'
new_cryptos_to_trade = update_list_in_file(cryptos_to_trade, file_path)


print (new_cryptos_to_trade)

#send_message("A long signal was found for the following coins: \n" + str(new_cryptos_to_trade))

print("Elapsed time: ", time.time() - start_time)

