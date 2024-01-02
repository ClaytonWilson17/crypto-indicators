from ta_api import *


#print (get_supertrend("BNB/USDT"))

#print (get_price_of_one_crypto("BNB/USDT"))


symbols = get_all_binance_symbols()

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

crytos_to_buy = []
for sym in symbols_more_than_10_cents:
    if (get_supertrend(sym, 12, 3)['valueAdvice']) == 'long':
        if (get_supertrend(sym, 10, 1)['valueAdvice']) == 'long':
            if (get_supertrend(sym, 11, 2)['valueAdvice']) == 'long':
                crytos_to_buy.append(sym)

print (crytos_to_buy)


