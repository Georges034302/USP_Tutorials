#!/bin/python3

s = 'USP Python Spr 2023'

print('Length = '+str(len(s)))
print(f'Length = {len(s)}')
print('First = '+s[0])
print('Last = '+s[len(s)-1])
print(s[0:6])

print(s.count('2'))
print(s.index('2'))
print(s.find('2'))
print(s.lower())
print(s.upper())
print(s.replace('Python','Java'))
print(s.isalpha())
print(s.isalnum())

