#!/bin/env python
#Register a number of users where each user has a unique ID (3 digits)
#A user is represent as key-value where key is the unique ID
#The ID is randomly generate and the value is from STDIN

import random as r
import pprint as pp 

n = int(input("Register: "))

keys = r.sample(range(100,999),n)  #list of random keys of size 3-digits

names = {}

for key in keys:
    names[key] = input("Name: ")

pp.pprint(names,indent=2,width=15)

key = int(input("Delete by key: "))
if key in keys:
    del names[key]
else:
    print("User does not exist!")

pp.pprint(names,indent=2,width=15)
