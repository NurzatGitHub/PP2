'''
If you have a Python object, you can convert it into a JSON string by using the json.dumps() method.

Example
'''

import json

x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

y = json.dumps(x)

print(y)

print(y[0])