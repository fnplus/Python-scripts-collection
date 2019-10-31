import requests
from bs4 import BeautifulSoup

url = input()

headers = {
    'User-Agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"
    }

response = requests.request("GET", url, headers = headers)

data = BeautifulSoup(response.text, 'html.parser')

images = data.find_all('img', src=True)

for image in images:
	print(image)
    