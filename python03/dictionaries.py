#!/bin/env python
#Dictionary is a collection of data as: key-value association
#Dictionary is unordered
#Dictionary is indexed
#Dictionary is changeable
#Dictionary does not allow duplicate keys

import pprint as pp 

mydictionary = {
    "ID":123,
    "Name":"Tom",
    "Age":30,
    "Role":"Student"
}

print(mydictionary)
print(mydictionary["Role"])

for key in mydictionary.keys():
    print(f'{key} :: {mydictionary[key]}')

pp.pprint(mydictionary,indent=4,width=10)

del mydictionary["Role"]
print(mydictionary)

