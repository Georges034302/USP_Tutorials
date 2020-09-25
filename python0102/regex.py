#!/bin/env python3

import re

txt = '''01-Welcome to Python 01 and 02
         This week USP is combines 02 tutorials 
         2020 usp spring session02'''

print("Finding 2 digits in a text--------------------------------------------")
print("Matching  2-digits: ",end=" ")
x = re.match("\d{2}",txt)
print(x)
print("Searching 2-digits: ",end=" ")
x = re.search("\d{2}",txt)
print(x)
print()

print("Finding 2 digits at the beginnning-------------------------------------")
x = re.search("^\d{2}",txt)
print(x)
x = re.search("^\d{2}",txt)
print(x)
print()

print("Finding 2 digits at the end--------------------------------------------")
x = re.search("\d{2}$",txt)
print(x)
x = re.match("\d{2}$",txt)
print(x)
print()

print("AND and OR operators---------------------------------------------------")
x = re.search("^\d{2}|\d{2}$",txt)
print(x)
x = re.search("^\d{2}.*\d{2}$",txt)
print(x)
x = re.match("^\d{2}|\d{2}$",txt)
print(x)
x = re.match("^\d{2}.*\d{2}$",txt)
print(x)
print()

print("ignore case in a pattern-----------------------------------------------")
x = re.search("USP",txt, re.IGNORECASE)
print(x)
print(x.span())
print(x.group())
print()

print("substitute all matches-------------------------------------------------")
x = re.sub("USP","Python",txt, flags=re.IGNORECASE)
print(x)
print() 



    
