#!/bin/env python3
#Set is a collection of Data unordered, unindexed and unchangeable
#Set does not allow duplicates

set1 = {"Weclome", "to", "USP"}
print(set1)

try:
    print(set1[1])
except TypeError:
    print("Sets are unordered and unindexed!!!")

print(">>> 1-  update a set")
set1.add(32547)
print(set1)
set1.update(["Spring",2020])
print(set1)

print(">>> 2- deleting elements from a set")
set1.remove(2020)
print(set1)

set1.discard("Spring")
print(set1)

set1.pop()
print(set1)

print(">>> 3- joining 2 sets")
set2 = {"Spring",2020}
myset = set1.union(set2)
print(myset)
set1.update(set2)
print(set1)


print(">>> 4- deleting a set")
del set1
try:
    print(set1)
except NameError:
    print("set1 has been deleted")

print(">>> Iterate a set")
for x in myset:
    print(x, end=", ")
print()

itset = iter(myset)
for x in itset:
    print(x, end=", ")
print() 

for x in enumerate(myset):
    print(x)
print()











