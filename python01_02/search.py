#!/bin/env python3
import re 

s = 'UTS FEIT spring 2024 - USP 32547 python3'

# Read target pattern from STDIN until .  
# Read replacement from STIDN 
# replace all occurrences of the pattern in the string 

pattern = input('Pattern: ')

while pattern != '.':
    replacement = input('replacement: ')
    print(re.sub(pattern,replacement,s))
    pattern = input('Pattern: ')
    

