from urllib.request import urlopen
import requests
import json
import operator
from bs4 import BeautifulSoup

# bittrex api, we hit the currency we want to trade
bittrexWebPage = requests.get("https://bittrex.com/api/v1.1/public/getorderbook?market=BTC-LTC&type=both&depth=2")

dataTradingBook = bittrexWebPage.json()

print(json.dumps(dataTradingBook, indent=4, sort_keys=True))