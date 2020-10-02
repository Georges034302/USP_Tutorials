#!/bin/env python3
#Dictionary is a collection unordered, indexed, changeable
#Dictionary does not allow duplicates


#create a dynamic dictionary of students names using 
#a random sample of 3 digits key
#names are from user input and the dictionary is key:name
#representation
import random as ran 

names = {}

print(">>> 1- generate a random sample")
keys = ran.sample(range(100,999),5)
print(keys)
print(">>> 2- dynamically populating a dictionary")
for key in keys:
    names[key] = input("Name: ")
print(names)

print(">>> 3- sorting a dictionary by keys")
for key in sorted(names.keys()):
    print("%s :: %s"%(key,names[key]))

print(">>> 4- deleting an element by key from a dictionary")
key = int(input("Delete by key: "))

if key in keys:
    del names[key]
else:
    print("Student does not exist!!!")

for key in sorted(names.keys()):
    print("%s :: %s"%(key,names[key]))










