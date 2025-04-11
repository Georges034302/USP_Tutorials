#!/bin/env python3
# Read a string from STDIN until .
# Count the vowels and show the total number of vowels

s = input('String: ')

while s != '.':
    total = 0
    for c in 'aeiou':
        frequency = s.lower().count(c)
        total += frequency
        print(f'{c} --> {frequency}')
    print(f'Total vowels = {total}')
    s = input('String: ')

