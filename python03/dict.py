#!/bin/env python3
#Dictionary is a collection of data
#Dictionary is unordered, indexed, changeable
#Dictionary allows duplication

#Create a script that generates a dymanic student record using a sample of 3-digits key
#Student names are entered by User
#Student record is stored into a dictionary [key:name] representation

import random as ran

names = {} #empty dictionary

print("Generate five random 3-digits sample keys: ")
keys = ran.sample(range(100,999),5) #returns a list of five keys randomly generated
print(keys)

print("Dynamically populate the student record: ")
for key in keys:
    names[key] = input("Name: ")
print(names)

print("Sorting the students record")
for key in sorted(names.keys()):
    print("%s-->%s"%(key,names[key]))

print("Delete student by ID")
key = int(input("Key: "))
if key in keys:
    del names[key]
else:
    print("Student record does not exist")

print("Sorting the students record")
for key in sorted(names.keys()):
    print("%s-->%s"%(key,names[key]))
