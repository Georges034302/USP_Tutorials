#!/bin/env python3
import re

txt = '''01-Welcome to USP 32547         
         This is week 09
         This week we will do P0203'''

x = re.search("\d{2}",txt)
print(x)
print(x.span())
print(x.group())
x = re.findall("[A-Z]",txt)
print(x)
x = re.sub("\s",".",txt)
print(x)
