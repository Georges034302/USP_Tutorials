#!/bin/env python3
#Set is a collection of data
#Set is unordered, unindexed, unchangeable
#Set does not allow duplication

set1 = {"Welcome","to","USP"}
print(set1)

try:
    print(set1[0])
except TypeError:
    print("Sets are not indexed!!!!!")

set1.add(32547) #adds element anywhere in the set
print(set1)

set1.update(["Aut",2021]) #adds collection-elements anywhere in the set
print(set1)

set1.remove("Aut")
print(set1)

set1.discard("to")
print(set1)

set1.pop() #removes the last element 
print(set1)

#Joining sorted
set2 = {"Python","Tut3"}
myset = set1.union(set2) #joins set1 and set2
print(myset)
set1.update(set2) #joins set2 into set1
print(set1)

del set1
try:
    print(set1)
except NameError:
    print("NameError: name 'set1' is not defined")

for e in myset:
    print(e, end=" ")
print()

for e in enumerate(myset):
    print(e, end=" ")
print()












