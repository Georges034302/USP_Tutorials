#!/bin/env python3

# Dictionary is a collection of data, formatted as key-->value
# Dictionary is not ordered
# Dictionary is not indexed (but we can read items by key)
# Dictionary keys are unique, values can be duplicated
# Dictionary is mutable --> CRUD
# Syntax: data = {
#                   key0: value0,
#                   key1: value1,
#                   ....
#                   keyn:valuen
#                   }
import pprint as pp


data = {
    'name':'Lucy',
    'age':28,
    'salary': 120000
}

print(data)             # showing a dictionary
print()

data['role'] = 'Admin'  # add item 
print(data)
print()
pp.pprint(data,width=40)
print()

del data['salary']
pp.pprint(data,width=40)
print()

del data
try:
    print(data)
except NameError:
    print('data is deleted')