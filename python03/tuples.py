#!/bin/env python3 
# Tuple is a data collection of different types
# Tuple is ordered 
# Tuple is indexed
# Tuple is unchangeable 
# Tuple allows duplicates 

tuple1 = ("Tom", "Smith", 22, True)
print(tuple1)

length = len(tuple1)
print("Length = ",length)

print("first = {}".format(tuple1[0]))
print("slice(1,3) = {}".format(tuple1[1:3]))

del tuple1
try:
    print(tuple1)
except NameError:
    print("tupe is deleted")
