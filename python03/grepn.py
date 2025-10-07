#!/bin/env python3
# Read a pattern from STDIN
# Show all the matching lines (with line numbers)
# Target is a file (filename from STDIN)
import re 

filename = input('filename: ')
regex = input('pattern: ')
found = False # flag

with open(filename, 'r') as handler:
    lines = handler.readlines()

for line_num, line in enumerate(lines,start=1):
    matches = re.findall(regex, line)
    if matches:
        found = True # matches found 
        print(f'{line_num} - {line.strip()}')
        for matching_line in matches:
            print(f' Match: {matching_line}')



