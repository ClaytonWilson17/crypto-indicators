# retrieves all of the technical indicators needed to determine buy and sell signals

# documentation to help know how to use the python module: 
#  https://python-tradingview-ta.readthedocs.io/en/latest/usage.html
#  https://tvdb.brianthe.dev/
#  https://python-tradingview-ta.readthedocs.io/_/downloads/en/latest/pdf/
#  https://pastebin.com/1DjWv2Hd

from tradingview_ta import TA_Handler, Interval
import itertools
import csv
import pandas as pd