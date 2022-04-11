#!/bin/env python3 

s = "...Welcome to Aut2022 - Python..."
length = len(s) 

print(f'Length of s = {length}')
print("First = ",s[0])
print("Last = ",s[length-1])
print(s.index("A"))
print(s.index("Aut"))
print(s.find("A"))
print(s.find("2022"))
print(s[11:])
print(s[11:length])
print(s[11:14])

print(s.lower())
print(s.upper())

print(s.count("o"))

print(s.replace("-","$"))
print(s.replace("Python","Perl"))

print(s.isalpha())
print(s.isdigit())
print(s.isalnum())
print(s.strip("."))
s1 = s.strip(".")
print(s1)

print(s1.split(" "))
print(s1.split("-"))





