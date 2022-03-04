import binance.client
from binance.client import Client
import json

client = Client(api_key = "", api_secret = "")

info = client.get_exchange_info()
symbols = info["symbols"]
all_tickers = []

for symbol in symbols:
    all_tickers.append(symbol["symbol"])

tickers_category = {}
my_assets = ["BTC", "USDT", "ETH", "BUSD"]

for asset in my_assets:
    tickers_category[asset] = []
    for ticker in all_tickers:
        if ticker.endswith(asset):
            tickers_category[asset].append(ticker)

string_json = json.dumps(tickers_category, indent = 4)

with open("tickers.json", "w") as outfile:
    outfile.write(string_json)

print("done!")
