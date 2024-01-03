from ta_api import *
import time
start_time = time.time()

res = get_EMA('NFP/USDT', 200)

print (res)

print("Elapsed time: ", time.time() - start_time)
