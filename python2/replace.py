#!/bin/python3
# Req: read a string until *
# Read in a search pattern
# Read in a replacement 
# Replace the pattern with the replacement
import re 
s = input('String: ')

while s != '*':
    pattern = input('Pattern: ')
    replacement = input('Replacement: ')
    text = re.sub(pattern,replacement,s)
    print(text)
    s = input('String: ')
