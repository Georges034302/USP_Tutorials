#!/bin/env python3

import re

s = 'Python 3 is cool, java 17 is fun'

print(re.search('o',s)) # find the position of the first occurrence
pattern = input('Pattern: ')
print(re.findall(pattern,s)) # similar to grep

replacement = input('Replacement: ')
print(re.sub(pattern,replacement,s)) # similar to sed





