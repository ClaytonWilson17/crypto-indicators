from ta_api import *
from send_discord_message import *


#print (get_supertrend("BNB/USDT"))

#print (get_price_of_one_crypto("BNB/USDT"))


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

cryptos_to_buy = []
for sym in all_binance_symbols:
    supertrend1 = get_supertrend(sym, 12, 3)['valueAdvice']
    supertrend2 = get_supertrend(sym, 10, 1)['valueAdvice']
    supertrend3 = get_supertrend(sym, 11, 2)['valueAdvice']
    if supertrend1 == 'long':
        supertrend1 = 1
    else:
        supertrend1 = 0

    if supertrend2 == 'long':
            supertrend2 = 1
    else:
        supertrend2 = 0

    if supertrend3 == 'long':
            supertrend3 = 1
    else:
        supertrend3 = 0

    if (supertrend1 + supertrend2 + supertrend3) > 1:
         price = get_price_of_one_crypto(sym)
         if price > get_EMA(sym, 200):
            if get_rsi(sym) < float(40):
                cryptos_to_buy.append(sym)



print (cryptos_to_buy)

send_message(str(cryptos_to_buy))



