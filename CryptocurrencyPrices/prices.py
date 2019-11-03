import re
import requests
import textwrap
import time

from bs4 import BeautifulSoup as bs


COINS = [
    'BTC', 'ETH', 'XRP', 'EOS',
    'BCH', 'LTC', 'XLM', 'DASH'
    'XTZ', 'ETC', 'USDC', 'BAT',
    'ZEC', 'ZRX', 'REP', 'DAI',
]
print("Available Coins")
print(COINS)

user_coin = input("Enter the coin: ")

while user_coin not in COINS:
    print("your coin not in list")
    user_coin = input("Enter the coin:")

response = requests.get("https://www.coinbase.com/price/{}".format(user_coin.lower()))
soup = bs(response.text, 'html.parser')
price = soup.find("div", {"class": "ChartPriceHeader__BigAmount-sc-9ry7zl-4 dKeshi"})
current_time = time.strftime("%b %Y %H:%M:%S", time.gmtime())
print("At {} price of {} is {}".format(current_time, user_coin, price.text))
