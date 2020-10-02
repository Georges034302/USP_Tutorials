#!/bin/env python3
#Tuple is a collection ordered, indexed and unchangeable
#Tuple allows duplicates

tuple1 = ("Welcome","to","USP")

print(">>> 1- Accesing elements from a tuple")
print(tuple1[1])
print(tuple1[len(tuple1)-1])
print(tuple1[0:2])
print(tuple1[:2])
print(tuple1[-2])

print(">>> 2- joining 2 tuples")
tuple2 = (32547,"Spring",2020)

mytuple = tuple1 + tuple2
print(mytuple)

print(">>> 2- deleting a tuple")
del tuple1
try:
    print(tuple1)
except NameError:
    print("tuple1 is deleted!!")

print(">>> 4- iterate a tuple")
for x in mytuple:
    print(x, end=", ")
print()

ittuple = iter(mytuple)
for x in ittuple:
    print(x, end=", ")
print()

for x in enumerate(mytuple):
    print(x)


