#!/bin/env python3

import re 

f = open("demo.txt","r")
regex = input("Pattern: ")
replacement = input("Replacement: ")

for txt in f:
    x = re.findall(regex,txt)
    if(x):
        x = re.sub(regex,replacement,txt)
        print(x)
f.close();
