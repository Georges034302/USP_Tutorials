#!/bin/env python3

import re 
# Read characters from STDIN
# check if the character is a digit 
# If it is a digit replace with $

c = input('Character: ')

if c.isdigit():
    print(re.sub('\\d','$',c))
else:
    print('Not a digit')
