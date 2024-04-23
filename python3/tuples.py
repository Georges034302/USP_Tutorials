#!/bin/env python3

# Tuple is a collection of data of any type
# Tuple is ordered
# Tuple is indexed
# Tuple allows duplicates
# Tuple is immutable
# Syntax: tuple_name = (item_0, item_1, ..., item_length-1)

tuple1 = ('UTS', 'Spr',2024,False)

print(len(tuple1))     
print(tuple1)               # print the tuple
print(tuple1[0])            # print first element
print(tuple1[-1])           # print last element
print(tuple1[len(tuple1)-1]) # print last element
print(tuple1[1:]) # print all elements from position 1


tuple2 = ('USP',32547)
total = tuple1 + tuple2
print(total)

del tuple1
try:
    print(tuple1)
except NameError:
    print('Tuple is deleted')

