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


# NASDAQ Stocks
nasdaq_stocks = [
    "ADBE", "ADP", "ABNB", "ALGN", "GOOGL", "GOOG", "AMZN", "AMD", "AEP", "AMGN",
    "ADI", "ANSS", "AAPL", "AMAT", "ASML", "AZN", "TEAM", "ADSK", "BKR", "BIIB",
    "BKNG", "AVGO", "CDNS", "CHTR", "CTAS", "CSCO", "CTSH", "CMCSA", "CEG", "CPRT",
    "CSGP", "COST", "CRWD", "CSX", "DDOG", "DXCM", "FANG", "DLTR", "EBAY", "EA",
    "ENPH", "EXC", "FAST", "FTNT", "GEHC", "GILD", "GFS", "HON", "IDXX", "ILMN",
    "INTC", "INTU", "ISRG", "KDP", "KLAC", "KHC", "LRCX", "LULU", "MAR", "MRVL",
    "MELI", "META", "MCHP", "MU", "MSFT", "MRNA", "MDLZ", "MNST", "NFLX", "NVDA",
    "NXPI", "ORLY", "ODFL", "ON", "PCAR", "PANW", "PAYX", "PYPL", "PDD", "PEP",
    "QCOM", "REGN", "ROST", "SIRI", "SBUX", "SNPS", "TMUS", "TSLA", "TXN", "VRSK",
    "VRTX", "WBA", "WBD", "WDAY", "XEL", "ZS"
]

# NYSE Stocks
nyse_stocks = [
    "ABT", "ABBV", "ACN", "ADM", "AES", "AFL", "A", "APD", "ALB",
    "ARE", "ALLE", "ALL", "MO", "AMCR", "AEE", "AXP", "AIG",
    "AMT", "AWK", "AMP", "AME", "APH", "AON", "APA", "APTV", "ACGL", "ANET",
    "AJG", "AIZ", "T", "ATO", "AZO", "AVB", "AVY", "AXON", "BALL", "BAC",
    "BBWI", "BAX", "BDX", "WRB", "BRK-B", "BBY", "BIO", "TECH", "BLK", "BK",
    "BA", "BWA", "BXP", "BSX", "BMY", "BR", "BRO", "BF-B", "BG", "CHRW",
    "CZR", "CPT", "CPB", "COF", "CAH", "KMX", "CCL", "CARR", "CTLT", "CAT",
    "CBOE", "CBRE", "CDW", "CE", "CNC", "CNP", "CF", "CRL", "SCHW", "CVX",
    "CMG", "CB", "CHD", "CI", "CINF", "C", "CFG", "CLX", "CME", "CMS", "KO",
    "CL", "CMA", "CAG", "COP", "ED", "STZ", "COO", "GLW", "CTVA", "CTRA", "CCI",
    "CMI", "CVS", "DHI", "DHR", "DRI", "DVA", "DE", "DAL", "XRAY", "DVN", "DLR",
    "DFS", "DIS", "DG", "D", "DPZ", "DOV", "DOW", "DTE", "DUK", "DD", "EMN", "ETN",
    "ECL", "EIX", "EW", "ELV", "LLY", "EMR", "ETR", "EOG", "EPAM", "EQT", "EFX",
    "EQIX", "EQR", "ESS", "EL", "ETSY", "EVRG", "ES", "EXPE", "EXPD", "EXR", "XOM",
    "FFIV", "FDS", "FICO", "FRT", "FDX", "FITB", "FSLR", "FE", "FIS", "FI", "FLT",
    "FMC", "F", "FTV", "FOXA", "FOX", "BEN", "FCX", "GRMN", "IT", "GEN", "GNRC",
    "GD", "GE", "GIS", "GM", "GPC", "GL", "GPN", "GS", "HAL", "HIG", "HAS", "HCA",
    "PEAK", "HSIC", "HSY", "HES", "HPE", "HLT", "HOLX", "HD", "HRL", "HST", "HWM",
    "HPQ", "HUM", "HBAN", "HII", "IBM", "IEX", "ITW", "INCY", "IR", "PODD", "ICE",
    "IFF", "IP", "IPG", "IVZ", "INVH", "IQV", "IRM", "JBHT", "JKHY", "J", "JNJ",
    "JCI", "JPM", "JNPR", "K", "KEY", "KEYS", "KMB", "KIM", "KMI", "KR", "LHX",
    "LH", "LW", "LVS", "LDOS", "LEN", "LIN", "LYV", "LKQ", "LMT", "L", "LOW",
    "LYB", "MTB", "MRO", "MPC", "MKTX", "MMC", "MLM", "MAS", "MA", "MTCH", "MKC",
    "MCD", "MCK", "MDT", "MRK", "MET", "MTD", "MGM", "MAA", "MHK", "MOH", "TAP",
    "MPWR", "MCO", "MS", "MOS", "MSI", "MSCI", "NDAQ", "NTAP", "NEM", "NWSA", "NWS",
    "NEE", "NKE", "NI", "NDSN", "NSC", "NTRS", "NOC", "NCLH", "NRG", "NUE", "NVR",
    "OXY", "OMC", "OKE", "OR"
]

stocks = get_tech_indicators(nyse_stocks, nasdaq_stocks)

stocks_to_long = []

for stock in stocks:
    try:
        signal = determine_signal(stock)
        if signal == 'long':
            stocks_to_long.append(stock['Symbol'])
    except:
        None

file_path = 'stocks_with_long_signal.txt'
new_stocks_to_long = update_list_in_file(stocks_to_long, file_path)
past_long_signals = read_txt_file(file_path)

print (new_stocks_to_long)




