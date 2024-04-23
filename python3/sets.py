#!/bin/env python3

# Set is a collection of data of any type
# Set is not ordered
# Set is not indexed
# Set does not allow duplicates
# Set is changeable
# Syntax: set_name = {item, item, item, ..., item}

set1 = {'Tom',34,14.5,True}

print(set1) # elements are randomly printed

set1.add('$')
print(set1)

set2 = {'UTS',2024}
total = set1.union(set2) # combine set1 and set2
print(total)

set1.add('Tom') # No duplicates allowec
print(set1)

set1.remove(34) # Delete by name
print(set1)

set1.discard('Tom') # Delete by name
print(set1)

set1.pop() # delete a random element
print(set1)

set1.clear() # remove all elements
print(set1)

del set1
try:
    print(set1)
except NameError:
    print('set1 is deleted!!!')


