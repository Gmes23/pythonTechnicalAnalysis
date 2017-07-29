import requests
import json


bittrexOrderBook =  requests.get("https://bittrex.com/api/v1.1/public/getorderbook?market=BTC-ANS&type=both&depth=10").json()
# print(bittrexOrderBook['result']['sell'][0]['Rate'])

for i in bittrexOrderBook['result']['sell'][:3]:
    print(i['Rate'])
# data = bittrexPerMinApi.json()
# data = bittrexOrderBook.json()

# for i in data['result']:
#     print(i)
# get open of stock, compare it to high of last day
# check min, buy min high
# if order does not complete in 2mins check order nook highest, order order book highest plus 200
# more, then sell for that price plus 600
# if stock is too high a price