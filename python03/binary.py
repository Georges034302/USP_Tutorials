#!/bin/env python3

# Read an integer between 0 and 255
# Convert this integer to IPv4 (8bits)

n = int(input('n = '))

zeros = [0,0,0,0,0,0,0,0]
my_list = []

while n > 0:
    my_list.append(n%2)
    n = int(n/2)
# print(my_list) # this is the reversed binary
reverse = list(reversed(my_list)) # This is the real binary
print(reverse)

binary = zeros[len(reverse):len(zeros)] + reverse
print(binary)

