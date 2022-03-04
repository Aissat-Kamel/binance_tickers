import json

with open("tickers.json", "r") as file:
    tickers = json.load(file)

btc_tickers = tickers["BTC"]
usdt_tickers = tickers["USDT"]
eth_tickers = tickers["ETH"]


usdt_lists = []
for i in range(0, len(usdt_tickers), 10):
    usdt_lists.append(usdt_tickers[i: i+10])


btc_lists = []
for i in range(0, len(btc_tickers), 10):
    btc_lists.append(btc_tickers[i: i+10])
