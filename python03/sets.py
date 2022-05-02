#!/bin/env python3 
# Set is a collection of data of different types
# Set is unordered 
# Set is not indexed
# Set is unchangeable
# Set elements are unique (no duplicates)

myset = {"USP", 32547, "Aut",2022, "Python", 3}     #creating a set 
print(myset)                                        #set is shuffled randomly at every print

myset.add(True)                                     #adding element to set 
print(myset)
myset.update([1.5,"Tom"])                           #adding a collection to set 
print(myset)

myset.remove(1.5)                                   #find and delete an element
print(myset)
myset.discard(3)                                    #find and delete an element
print(myset)
myset.pop()                                         #remove random element
print(myset)

set2 = {"new", "world"}
myset.update(set2)
print(myset)

del set2
try:
    print(set2)
except NameError:
    print("set2 does not exist!!!!")

for e in enumerate(myset):
    print(e)



