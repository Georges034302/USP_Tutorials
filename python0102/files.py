#!/bin/env python3
import sys
import re

op = input("Choice: c (continue) x (exit): ")

while op != "x":
    f=open("demo.txt","r")
    regex = input("Pattern: ")
    replace = input("Replacement: ")
    for txt in f:
        x = re.findall(regex,txt)
        if(x):        
            x = re.sub(regex,replace,txt)
            print(x)
    f.close()
    op = input("Choice: c (continue) x (exit): ")
    

print("Thank you: Bye")
