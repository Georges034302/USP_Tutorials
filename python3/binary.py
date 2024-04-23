#!/bin/env python3

# Read an integer between 0 and 255
# Convert the integer to IPv4 (8 bits)

n = int(input('n = '))

mylist = []
zeroes = [0,0,0,0,0,0,0,0]

while n > 0:
    mylist.append(n%2)
    n = int(n/2)

print(mylist)

reverse = list(reversed(mylist))
print(reverse)

binary = zeroes[len(reverse):len(zeroes)] + reverse
print(binary)