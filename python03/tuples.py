#!/bin/env python
#Tuple is a collection of data
#Tuple is ordered
#Tuple is indexed
#Tuple is not changeable
#Tuple allows duplicates

mytuple = ("Tom",30,10.5)           #Creating a Tuple

print(mytuple[0])                   #Accessing first element 
print(mytuple[len(mytuple)-1])      #Accessing last element

tuple2 = tuple(("dollar"))
print(tuple2)

newtuple = mytuple + tuple2;        #Joining two tuples
print(newtuple)

print(newtuple.count('l'))          #count the occurences of an object

del newtuple

try:
    print(newtuple)
except NameError:
    print("tuple was deleted")
