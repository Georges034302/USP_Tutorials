#!/bin/env python3

# Set is a collection of data of any type
# Set is not ordered
# Set is not indexed
# Set does not allow duplicates
# Set is changeable
# Syntax: set_name = {item, item, item, ..., item}

my_set = {'AWS', 2024, 22.5, True}
print(my_set)

my_set.add('$')
print(my_set)

other_set = {'$','AWS','Python'}
total = my_set.union(other_set)
print(total)

total.pop()
print(total)
total.remove(2024)
print(total)
total.discard(22.5)
print(total)
total.clear()
print(total)







