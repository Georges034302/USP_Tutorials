#!/bin/env python3

import re

s = 'Python 10 is easier than Java 17'

pattern = input('Pattern: ')

print(re.search(pattern,s)) # returns the first matching pattern
print(re.match(pattern,s)) # returns first occurence of a pattern
print(re.findall(pattern,s)) # returns all matching patterns - similar to grep
replacement = input('Replacement: ')
print(re.sub(pattern,replacement,s)) # Search and transform - similar to sed




