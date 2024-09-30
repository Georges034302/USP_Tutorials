#!/bin/env python3

# Dictionary is a collection of data, formatted as key-->value
# Dictionary is ordered (by key)
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
    'name':'Jason',
    'age': 36,
    'salary': 120000
}

print(data)
print(data['age'])

data['role'] = 'admin'
print(data)
data['department'] = 'HR'
print(data)

del data['department']
print(data)
pp.pprint(data,width=40)








