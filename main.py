import math
import requests


response = requests.get('https://yobit.net/api/3/ticker/eth_usdt-btc_usdt')  # Получаем json ответ из биржи
data = response.json()


eth_price = float(data['eth_usdt']['last'])  # Получение цен криптовалют
btc_price = float(data['btc_usdt']['last'])


print(f"Стоимость ETH : {eth_price:.2f} USDT")
print(f"Стоимость BTC : {btc_price:.2f} USDT")


eth_price_without_btc = eth_price / btc_price
eth_price_without_btc_in_pro = eth_price / btc_price * 100
price_eth = eth_price_without_btc_in_pro / 100  # с учетом вычета процентов
price_eth_pro = round(price_eth, 3) * eth_price
eth = eth_price - price_eth_pro


print(f"Стоимость без ETH влияния BTC составляет: {eth_price_without_btc:.2f} USDT")
print(f"Стоимость ETH без влияния BTC в процентном соотношении составляет: {eth_price_without_btc_in_pro:.2f}% USDT или {math.ceil(price_eth_pro)} USDT")
print(f"Стоимость ETH без влияния BTC : {eth:.2f} USDT")





# !!!!!!!!!!!{:.2f} - отображение чисел с разделением групп разрядов запятыми и двумя знаками после запятой.!!!!!!!!!