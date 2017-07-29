from lxml import html
import requests
import json
import numpy as np
import operator

# coinmarketcap api
#warning this must be updated everyday
coinmarketcapWebPage = requests.get("https://coinmarketcap.com/currencies/neo/historical-data/?start=20170721&end=20170727")

# We need to use page.content rather than page.text
# because html.fromstring implicitly expects bytes as input.
tree = html.fromstring(coinmarketcapWebPage.content)

# webData is every text in the td divs
webData = tree.xpath('//td/text()')

# separating the data into variables
date = webData[0::7]
dateOpen = webData[1::7]
dateHigh = webData[2::7]
dateLow = webData[3::7]
dateClose = webData[4::7]
dateVolume = webData[5::7]
dateMarketCap = webData[6::7]


firstFiveHigh = dateHigh[:3]
firstFiveLow = dateLow[:3]

avgHigh = [float(numeric_string) for numeric_string in firstFiveHigh]
avgLow = [float(numeric_string) for numeric_string in firstFiveLow]


realAvgHigh = sum(avgHigh)/len(avgHigh)
realAvgLow = sum(avgLow)/len(avgLow)

print(realAvgHigh)
print(realAvgLow)
# print(np.mean(firstTen))
# averageLow = sum(float(int(str(firstTen))))
# print(averageLow)
# print('dates ', date)
# print('open', dateOpen)
# print('high', dateHigh)
# print('low', dateLow)
# print('close', dateClose)
# print('Volume', dateVolume)
# print('MarketCap', dateMarketCap)
# print(averageLow)

# print('Data for coin: ', data)

# print(r.text)
# jsonCleaned = json.dumps(data, indent=4, sort_keys=True)
# print(json.dumps(data, indent=4, sort_keys=True))