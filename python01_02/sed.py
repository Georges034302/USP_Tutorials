#!/bin/env python3

# Read a string from STDIN until .
# Read a pattern
# Read a replacement
# Show the updated string

import re

s = input('string: ')

while s != '.':
    pattern = input('pattern: ')
    repl = input('replacement: ')
    txt = re.sub(pattern,repl,s,flags=re.IGNORECASE)
    print(txt)
    s = input('string: ')

