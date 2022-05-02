#!/bin/env python3 
#read data from file (filename is first argument)
#read a pattern
#read a replacement
#match the pattern with the file compile
#replace the matching patterns

import re 
import sys 

filename = sys.argv[1]
fin = open(filename)             #open the filename

pattern = input("Pattern: ")
replacement = input("Replacement: ")

for line in fin:
    found = re.findall(pattern,line)
    if(found):
        replacement = re.sub(pattern,replacement,line)
        print(replacement)
        
fin.close();
