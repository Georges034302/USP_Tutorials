#!/bin/env python3

import json
import pprint

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

pp = pprint.PrettyPrinter(indent=4)
pp.pprint(x)

y=json.dumps(x)

print(y)

z = json.dumps(x,indent=5, separators=("; "," == "),sort_keys=True)
print(z)




