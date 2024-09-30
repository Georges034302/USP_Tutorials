#!/bin/env python3

# List is a collection of data of any type
# List is ordered
# List is indexed
# List allows duplicates
# List is changeable --> CRUD
# Syntax: list_name = [item_0, item_1, ..., item_len-1]

list1 = ['Tom',34,22.8,True]

print(list1)
print(len(list1))
print(list1[0])
print(list1[-1])
print(list1[len(list1)-1])

list1.append('has')
print(list1)
list1.insert(2,'$')
print(list1)

list1.pop()
print(list1)
list1.pop(1)
print(list1)
list1.remove(True)
print(list1)

del list1
try:
    print(list1)
except NameError:
    print('list1 is deleted')

print('bye')






