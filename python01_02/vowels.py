#!/bin/env python3

# Read string from STDIN until . 
# Determine the vowel frequency in the string
# Determine the total number of vowels in the string 

s = input('string: ')
total = 0

while s != '.':
    for c in 'aeiouAEIUO':
        frequency = s.count(c)
        total += frequency
        print(f'{c} --> {frequency}')
    print(f'Total vowels in s = {total}')
    s = input('string: ')

