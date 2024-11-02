from mftool import Mftool
from yahooquery import Ticker, Screener
from json import dumps, loads
from fuzzywuzzy import fuzz, process

mf = Mftool()
scheme_details = mf.get_scheme_details(120716)
print(scheme_details)
scheme_name = scheme_details['scheme_name']


# a map of mutual fund name to code
mfMap = dict()

# read json file
with open('codes.json') as f:
    data = loads(f.read())
    for d in data:
        keys = list(d.keys())
        new_key = d[keys[0]]
        new_value = keys[0]
        mfMap[new_key] = new_value
        # break
# print(mfMap)



# print all keys which have a particular string
test = 'Parag Parikh'
results = search_closest_keys(test, mfMap)

# example of map and reduce
keys_with_bo_appended = list(map(lambda key: key+".BO", list(results.values())))
print(keys_with_bo_appended)

ticker_data = Ticker(keys_with_bo_appended)
holdings_data = ticker_data.fund_holding_info
for k, v in holdings_data.items():
    print(v.keys())
    holdings = v['holdings']
    print(v['equityHoldings'])
    break
    

# for k, v in results.items():
#     print(k, v)
#     ticker = Ticker(v+".BO")
#     print(ticker.summary_detail)
# for key in mfMap.keys():
#     if test.lower() in key:
#         print(key, mfMap[key])


# mf_ticker = Ticker('120716.BO')