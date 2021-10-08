#!/bin/env python3 
#Dictionary is a collection of data 
#Dictionary is unordered, indexed, changeable
#Dictionary does not allow duplicates 

#Create a dynamic dictionary of students 
#use random to generate random IDs (3 digits)
#Read the student names from STDIN and store them key:value in a dictionary

import random as r 

#Generate 3 digit sample IDs 
keys = r.sample(range(100,999),5)
print(keys)

#Dynamically populate a dictionary
names = {}
for key in keys:
    names[key] = input("Name: ")
print(names)

#Sorting a dictionary
for key in sorted(names.keys()):
    print("%s::%s"%(key,names[key]))

#Deleting element from a dictionary
key = int(input("Delete by key: "))

if key in keys:
    del names[key]
else:
    print("Student is not in the dictionary")

for key in sorted(names.keys()):
    print("%s::%s"%(key,names[key]))
