#!/bin/env python3 
#read a file (as argument) of strings
#count the number of words in the file

import sys 

filename = sys.argv[1]
fin = open(filename)             #open the filename

count = 0

for line in fin:
    count += len(line.split())

print(f'{filename} has {count} words')
