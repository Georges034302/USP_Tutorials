#!/bin/python3
# Set is unordered
# Set is not indexed
# Set is changeable
# Set does not allow duplicates

set1 = {'UTS','FEIT',2023,'oct',11}

print(set1)

set1.add('UTS')
print(set1)

set2 = {'mark',80}
set1.update(set2)
# set1.union(set2)
print(set1)

set1.remove('UTS')
print(set1)
set1.discard(11)
print(set1)
set1.pop()
print(set1)





