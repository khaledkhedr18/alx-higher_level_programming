import json

jsonnn = json.dumps([1, 2, 3, {'4': 5}, {'5': 6}], separators=(',', ': '))

print(jsonnn)

khaledjson = json.loads()