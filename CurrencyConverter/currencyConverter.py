import requests

print("Press Enter to exit the program \n")
currency_code = input("Currency you want to convert : ").lower()
url = f'http://www.floatrates.com/daily/{currency_code}.json'
r = requests.get(url).json()
dct_currencies = {}

if currency_code != 'usd':
    dct_currencies['usd'] = float(r['usd']['rate'])
if currency_code != 'eur':
    dct_currencies['eur'] = float(r['eur']['rate'])


while True:
    received_code = input("Currency you want to convert to : ").lower()
    if received_code == '':
        break
    amount = int(input("Enter amount : "))
    received_rate = float(r[received_code]['rate'])
    dct_currencies[received_code] = received_rate
    result = round(amount * received_rate, 2)
    print(f'You received {result} {received_code.upper()}.')