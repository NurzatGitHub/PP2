'''
Parse JSON - Convert from JSON to Python
If you have a JSON string, you can parse it by using the json.loads() method.
'''

import json

x = '{ "name":"John", "age":30, "city":"New York"}'

y = json.loads(x)

print(y['age'])
print(y['name'])