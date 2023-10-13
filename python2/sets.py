#!/bin/python3
# Set is a collection of values
# Set values are unique
# Set is not ordered
# Set is not indexed 
# Set is changeable

s = {'Tom',33,'has',22.5}

print(s)

s.add('balance')
print(s)

s.add('balance') # only one balance exists
print(s)

s.update({'account','CBA'})
print(s)

s.remove('CBA')
print(s)
s.discard('account')
print(s)

s.pop()
print(s)

s3 = s.copy()
print(s3)
s.add(123)
print(s3)

del s

try:
    print(s)
except NameError:
    print('sorry s is deleted')

