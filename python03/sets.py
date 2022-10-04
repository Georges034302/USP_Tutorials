#!/bin/env python
#Set is a collection of data
#Set is unordered
#Set is un-indexed
#Set is changeable
#Set does not allow duplicates

myset = {"USP","Spring",2022}       #Creating a Set
print(myset)

myset.add("Python")                 #Add an element at no specific order
print(myset)

mylist = ["UTS", "FEIT"]
myset.update(mylist)                #Adding a collection to the set
print(myset)

myset.remove("FEIT")                #Remove object from the set
print(myset)

myset.discard("Spring")             #Remove object from the set
print(myset)

myset.pop()                         #Remove the last element (at this time)
print(myset)


set2 = {"Spring","Autumn"}

newset = myset.union(set2)          #Joining two sets
print(newset)

del newset
try:
    print(newset)
except NameError:
    print("newset does not exist")

myset.add(5)                        #No duplicates allowed
myset.add(5)
myset.add(5)
myset.add(5)

print(myset)














