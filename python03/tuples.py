#!/bin/env python3
#Tuple is a collection of data
#Tuple is ordered, indexed, but unchangeable
#Tuple allows duplciation

tuple1 = ("Welcome", "to", "USP")
print(tuple1)
print("First: "+tuple1[0])
print("Last: "+tuple1[len(tuple1)-1])
print("First two: "+str(tuple1[:2]))

tuple2 = (32547,"Aut",2021)

mytuple = tuple1 + tuple2
print(mytuple)

del tuple1
try:
    print(tuple1)
except NameError:
    print("tuple1 has been deleted!!!!")

for e in mytuple:
    print(e, end=" ")
print()
