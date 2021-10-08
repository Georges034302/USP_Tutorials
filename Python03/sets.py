#!/bin/env python3
#Set is a collection of data 
#A set is unordered, unindexed and unchangeable
#Set does not allow duplicates

#Creating a set
set1 = {"Welcome","to","USP"}
print(set1)

#Adding to a set
set1.add(32547)
print(set1)

set1.update(["Spring",2021])
print(set1)

#Deleting elements from a set
set1.remove(2021)
print(set1)

set1.discard("Spring")
print(set1)

set1.pop()
print(set1)

#Joining sets
set2 = {"Spring",2021}
myset = set1.union(set2)
print(myset)

set1.update(set2)
print(set1)

#Deleting a set   
del set1
try:
    print(set1)
except NameError:
    print("The set does not exist!")


#Iterate a set   
for e in myset:
    print(e,end=", ")
print()

#enumerate indexes a set  
for e in enumerate(myset):
    print(e)
print()
























