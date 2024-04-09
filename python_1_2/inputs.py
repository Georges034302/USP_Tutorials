#!/bin/env python3
import sys 

# Enter data into the script from STDIN
name = input('Enter your name: ')
print(f'Welcome {name}')

# Get data into the script using arguments
first = sys.argv[1]
second = sys.argv[2]
third = sys.argv[3]
print(f'{first} - {second} - {third}')