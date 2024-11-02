from json import loads

mfMap = dict()

with open('codes.json') as f:
    data = loads(f.read())
    for d in data:
        keys = list(d.keys())
        new_key = d[keys[0]]
        new_value = keys[0]
        mfMap[new_key] = new_value