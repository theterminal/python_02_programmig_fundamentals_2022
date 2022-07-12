# 20220618 - Python Code - Lists Advance - Lecture
# Notes - 08 - Additional Information - APIs

import json
import requests


# api key request
key_btc_usdt = "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"
key_eth_usdt = "https://api.binance.com/api/v3/ticker/price?symbol=ETHUSDT"
key_ltc_usdt = "https://api.binance.com/api/v3/ticker/price?symbol=LTCUSDT"
key_eur_usd = "https://api.binance.com/api/v3/ticker/price?symbol=EURUSD"

# request data from url
data_btc_usdt = requests.get(key_btc_usdt)
data_btc_usdt = data_btc_usdt.json()

data_eth_usdt = requests.get(key_eth_usdt)
data_eth_usdt = data_eth_usdt.json()

data_ltc_usdt = requests.get(key_ltc_usdt)
data_ltc_usdt = data_ltc_usdt.json()

data_eur_usd = requests.get(key_eur_usd)
data_eur_usd = data_eur_usd.json()

print(f"{data_btc_usdt['symbol']} price is {data_btc_usdt['price']}")
print(f"{data_eth_usdt['symbol']} price is {data_eth_usdt['price']}")
print(f"{data_ltc_usdt['symbol']} price is {data_ltc_usdt['price']}")
print(f"{data_eur_usd['symbol']} price is {data_eur_usd['price']}")
