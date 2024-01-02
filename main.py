from ta_api import *


#print (get_supertrend("BNB/USDT"))

#print (get_price_of_one_crypto("BNB/USDT"))


symbols = get_all_binance_symbols()
symbols = symbols[0:80]

symbols_more_than_10_cents = []
for sym in symbols:
    try:
        if 'USDT' in sym:
            price = get_price_of_one_crypto(sym)
            #if price > .1:
            symbols_more_than_10_cents.append(sym)
    except:
        None


print (symbols_more_than_10_cents)





