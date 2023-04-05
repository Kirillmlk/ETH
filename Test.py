import requests


eth_response = requests.get("https://yobit.net/api/3/ticker/eth_usdt")
btc_response = requests.get("https://yobit.net/api/3/ticker/btc_usdt")


eth_price = float(eth_response.json()["eth_usdt"]["last"])
btc_price = float(btc_response.json()["btc_usdt"]["last"])


eth_price_without_btc = eth_price - btc_price


eth_btc_percent = eth_price / btc_price * 100


print("ETH/USDT price: {:.2f} USDT".format(eth_price))
print("BTC/USDT price: {:.2f} USDT".format(btc_price))
print("ETH/USDT price without BTC/USDT influence: {:.2f} USDT".format(eth_price_without_btc))
print("ETH/BTC percentage: {:.2f}%".format(eth_btc_percent))