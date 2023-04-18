#!/bin/python3

i = 1
while i <= 10:
    print(f'{i:3} ---> {i**2:4}')
    i += 1

print()

for e in range(1,11):
    print(f'{e:3} ---> {pow(e,2):4}')
