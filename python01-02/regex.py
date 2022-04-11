#!/bin/env python3
import re


txt = \
"""
^Day05: SysAdmin, Debugging, RegEX in Python
1 - Lesson 1: Using re module from python library
2 - Lesson 2: SysAdmin commands from os Module
OS Module from Python has over 100 functions
3 - Lesson 3: Debugging python scripts$
^ NOTE: Today we will discuss python fundamentals 
25/03/2022 
"""

print(re.search("\d",txt))
print(re.match("\d",txt))
print(re.findall("\d",txt))

print(re.findall("-",txt))
print(re.findall("[A-Z]",txt))
print(re.findall("[0-9]{2}",txt))
print(re.findall("\d{2}",txt))

replaced = re.sub("python","Java",txt)
print(replaced)


replaced = re.sub("python","Java",txt,flags=re.IGNORECASE)
print(replaced)
