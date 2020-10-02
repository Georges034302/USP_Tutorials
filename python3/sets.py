#!/bin/env python3
#a Set is unordered and unchangeable collection
#a set does not allow duplicates

set1 = {"Welcome", "to", "USP"}
print(set1)

try:
    print(set1[1])
except TypeError:
    print("Sets are not indexed")

print(">>> 1 - update a set:")
set1.add("32547")
print(set1)
set1.update(["Spr",2020])
print(set1)

print(">>> 2 - Delete elements from a set:")
set1.remove(2020)
print(set1)
set1.discard("Spr")
print(set1)
set1.pop() 
print(set1)

print(">>> 3 - joining 2 sets:")
set2 = {"Spr", 2020}
myset = set1.union(set2)
print(myset)
set1.update(set2)
print(set1)

print(">>> 4 - deleting a set:")
del set1 

try:
    print(set1)
except NameError:
    print("set1 has been deleted!!")

print(">>> 5 - iterating a set:")
for x in myset:
    print(x, end=",")
print()

























