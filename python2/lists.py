#!/bin/python3
# List is changeable
# List is ordered
# List is indexed
# List allows duplicates

mylist = ['Tom',150.25,'$',True]

print(mylist)
print(len(mylist))
print(mylist[0])
print(mylist[len(mylist) - 1])
print(mylist[0:2])

mylist.append('balance')
print(mylist)
mylist.insert(1,'has')
print(mylist)

mylist.remove(True)
print(mylist)

mylist.pop(1)
print(mylist)

mylist.pop()
print(mylist)

mylist[1] = 'Cruise'
print(mylist)

other = [125.25,'dollars']
total = mylist + other
print(total)

total.clear()
print(total)

del total

try:
    print(total)
except NameError:
    print('total does not exist')
















