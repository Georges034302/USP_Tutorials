#!/bin/env python3

# Tuple is a collection of data of any type
# Tuple is ordered
# Tuple is indexed
# Tuple allows duplicates 
# Tuple is immutable (none changeable)
# Syntax: tuple_name = (item-0, item-1, ..., item-n)

my_tuple = ('USP',2024,'Python', 3)
print(my_tuple)
print(my_tuple[0])
print(my_tuple[-1])
print(my_tuple[0:2])

other = ('$',22.5)
total = my_tuple + other 
print(total)

del total
try:
    print(total)
except NameError:
    print('tutple is deleted')



