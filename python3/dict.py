#!/bin/env python3
#a dictionary is a collection unordered, changeable, indexed
#a dictionary does not allow duplicates
import random as ran 

names = {}

print("Random sampling:")
keys = ran.sample(range(100,999),5)

print(">>> 1 - dynamically populating a dictionary")
for key in keys:
    names[key] = input("Name: ")
print(names)

print(">>> 2 - sort a dictionary")
for key in sorted(names.keys()):
    print("%s :: %s"%(key,names[key]))

print(">>> 3 - delete an element")
rem = int(input("Delete by key: "))

if rem in keys:
    del names[rem]
else:
    print("Student does not exist!!!")

for key in sorted(names.keys()):
    print("%s :: %s"%(key,names[key]))


