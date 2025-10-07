#!/bin/env python3
# Read n integer between 0 and 255
# Convernt n to binary size 8-bits

n = int(input('n = '))

remainders = []

while n > 0:
    remainder = n%2
    remainders.append(remainder)
    n = int(n/2)

print(f'Inverse: {remainders}')
reverse = list(reversed(remainders))
print(f'Correct: {reverse}')
zeroes = [0,0,0,0,0,0,0,0]

binary = zeroes[len(reverse):len(zeroes)] + reverse
print(f'Binary: {binary}')
for e in binary:
    print(e,end=' ')
print()
