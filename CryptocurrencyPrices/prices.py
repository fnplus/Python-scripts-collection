import re
import requests
import time
import os

from bs4 import BeautifulSoup as bs


COINS = [
    'Bitcoin', 'Ethereum', 'Ripple',
    'EOS', 'Bitcoin-cash', 'Litecoin',
    'Stellar', 'DASH', 'Tezos',
    'Ethereum-Classic', 'USDC',
    'Basic-Attention-Token', 'Zcach',
    'Ox', 'Augur', 'Dai',
]

def num_align(index, coin):
    """This function is for making align
    coins name
    example:
    from:
    8: Tezos  ----------------------XTZ
    9: Ethereum Classic  -----------ETC
    10: USD Coin  -------------------USDC
    to:
    8:  Tezos  ----------------------XTZ
    9:  Ethereum Classic  -----------ETC
    10: USD Coin  -------------------USDC
    """
    if len(str(index)) == 2:
        width = (len(str(index)) - 1) + len(coin)
    else:
         width = (len(str(index)) + 1) + len(coin)
    return width

os.system('clear') # clear commandline from previous commands
print("Available Coins", end="\n\n")

for index, coin in enumerate(COINS):
    num = num_align(index, coin)
    print('\033[95m{}\033[00m:\033[92m{}\033[00m'.format(index, coin.rjust(num)))

print()
user_coin = int(input("Please enter the number of coin: "))
while user_coin >  len(COINS):
    # while answer is incorrect
    print("Your coin not in list")
    user_coin = int(input("Enter the correct coin number: "))

response = requests.get("https://www.coinbase.com/price/{}".format(COINS[user_coin]))
soup = bs(response.text, 'html.parser')
price = soup.find("div", {"class": "ChartPriceHeader__BigAmount-sc-9ry7zl-4 dKeshi"})
current_time = time.strftime("%b %Y %H:%M:%S", time.gmtime())
items = "\nAt \033[91m{}\033[00m price of \033[95m{}\033[00m is \033[92m{}\033[00m"
print(items.format(current_time, COINS[user_coin], price.text))
