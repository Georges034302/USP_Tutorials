#!/bin/env python3

# Read a string from STDIN until .
# Find and replace a pattern
# Read the replacement and pattern from STDIN

import re

s = input('string: ')

while s != '.':
    pattern = input('regex: ')
    repl = input('replacement: ')
    txt = re.sub(pattern, repl, s)
    print(txt)
    s = input('string: ')
