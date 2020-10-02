#!/bin/env python3
# tuple is a collection ordered and unchangeable
# tuple allows duplicate

tuple1 = ("Welcome", "to", "USP")
print(">>> 1 - Accessing a  tuple:")
print(tuple1[1])
print(tuple1[1:3])
print(tuple1[len(tuple1)-1])
print(tuple1[-2])

print(">>> 2 - joining 2 tuples:")
tuple2 = (32547,"Spr",2020)
mytuple = tuple1 + tuple2
print(mytuple)

print(">>> 3 - deleting a tuple:")
del tuple1
try:
    print(tuple1)
except NameError:
    print("tuple1 is deleted")

print(32547 in mytuple)

print(">>> 4 - iterate a tuple")
for x in mytuple:
    print(x, end=",")
print()

ittuple = iter(mytuple)
for x in ittuple:
    print(x, end=",")
print()

for x in enumerate(mytuple):
    print(x)







