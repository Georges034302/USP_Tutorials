#!/bin/env python3 
#Tuple is a collection of data 
#Tuples are ordered, indexed, and unchangeable
#Tuples allow duplicates 

tuple1 = ("Welcome","to","USP")

#Accessing elements 
print("First: "+tuple1[0])
print("Last: "+tuple1[len(tuple1)-1])
print(tuple1[:2])
print(tuple1[-2])

#Joining tuples 
tuple2 = ("Spring",2021)
mytuple = tuple1 + tuple2 

print(mytuple)

#delete a tuple   
del tuple1
try:
    print(tuple1)
except NameError:
    print("The tuple does not exist")
