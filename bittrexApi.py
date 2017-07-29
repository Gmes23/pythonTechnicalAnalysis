import requests
import json
import operator

# bittrex api
# r = requests.get("https://bittrex.com/api/v1.1/public/getcurrencies")
r = requests.get("https://bittrex.com/api/v1.1/public/getmarketsummaries")
data = r.json() 
# coinmarketplace api
rCMP = requests.get('https://api.coinmarketcap.com/v1/ticker/?limit=3')
data_from_CMP = rCMP.json()

# jsonCleaned = json.dumps(data, indent=4, sort_keys=True)
# print(json.dumps(data, indent=4, sort_keys=True))
print("***********************************")


bank = 1000
value_Of_BTC_in_USD = float(data_from_CMP[0]['price_usd'])
bank_In_BTC = (1/value_Of_BTC_in_USD) * bank

for i in data['result']:
    if i['MarketName'].startswith('BTC'):
        try:
            maximunCoinsPerBank = bank_In_BTC / float(i['Last'])
            maxProfitsMade_based_on_24hr_change = (maximunCoinsPerBank * float(i['High'])) - bank_In_BTC
            minProfitsMade_based_on_24hr_change = (maximunCoinsPerBank * float(i['Low'])) - bank_In_BTC
        except ZeroDivisionError:
            pass
        print('**** ' + i['MarketName'] + ' ****')
        print('volume in USD: ' + str(i['Volume']))
        print('current value in BTC : ' + str(float(i['Last'])) + ' btc')
        print('current value in USD : ' + str((float(i['Last']) * value_Of_BTC_in_USD)) + ' USD')
        print('maximun coins per ' + str(bank) + ' USD : ' + str(maximunCoinsPerBank) + ' ' + i['MarketName'])
        print('investment in btc : ' + str(bank_In_BTC))
        print('max profits based 24hr high in BTC : ' + str( maxProfitsMade_based_on_24hr_change) + ' satoshi')
        print('min profits based 24hr low in BTC : ' + str(minProfitsMade_based_on_24hr_change) + ' satoshi')
        print('max profits base on 24hr high in USD : ' + str((maxProfitsMade_based_on_24hr_change * value_Of_BTC_in_USD)) + ' USD')
        print('min profits based on 24hr low in USD : ' + str((minProfitsMade_based_on_24hr_change * value_Of_BTC_in_USD)) + ' USD')
        print('***********************************************************************')

        
