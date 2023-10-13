#!/bin/python3
# List is a collection of values
# List is indexed
# List is ordered
# List allows duplicates
# List is changeable

l = ['Tom', 'has', 22, '$']

print(len(l))
print(l[0])
print(l[len(l)-1])
print(l[1:3])

l.append('balance')
print(l)
l.insert(1,30)
print(l)
other = ['Oct', 13]
total = l + other
print(total)

total.remove('balance')
print(total)
total.pop(1)
print(total)
total.pop()
print(total)

total.clear()
print(total)

del total
try:
    print(total)
except NameError:
    print('total does not exist anymore')

print('the program continues')
print(l)

