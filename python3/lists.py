#!/bin/env python3

# List is a collection of data of any type
# List is ordered
# List is indexed
# List allows duplicates
# List is changeable --> CRUD
# Syntax: list_name = [item_0, item_1, ..., item_len-1]

list1 = ['Tom',34,55.80,True]

print(list1)        # showing the list
print(len(list1))   # determine the list length

# Read operations
print(list1[0])     # read first element
print(list1[-1])    # get last element from opposite direction
print(list1[len(list1)-1]) # get last element
print(list1[0:2])   # get elements at position 0 and 1

# Create operations
list1.append('has') # add element to the end of the list
print(list1)

list1.insert(2,'has') # inject an element at position 2
print(list1)

list2 = ['balance','$']
total = list1 + list2 # joining 2 lists
print(total)

# Update operations
list1[4] = False    # update element at position 4
print(list1)

# Delete Operations
list1.pop()         # deletes the last element
print(list1)

list1.pop(1)        # deletes element at position 1
print(list1)

list1.remove(False) # Remove an object
print(list1)

list1.clear()       # Remove all objects
print(list1)

del list1           # Delete the list itself

try:
    print(list1)
except NameError:
    print(f'list1 does not exist')

print(total)




