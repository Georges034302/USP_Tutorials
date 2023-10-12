#!/bin/python3
# Req: Read a string until -1
# replace any pattern with string from STDIN
import re 
s = input('String: ')

while s != '-1':
    pattern = input('Pattern: ')
    replacement = input('Replacement: ')
    print(s)
    text = re.sub(pattern,replacement,s)
    print(text)

    s = input('String: ')
