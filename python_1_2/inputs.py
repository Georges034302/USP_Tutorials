#!/bin/env python3
import sys 

# Method 1: get values into script using STDIN
name = input('Enter your name: ')
print(name)

# Method 2: get values from arguments
first = sys.argv[1]
second = sys.argv[2]
third = sys.argv[3]
print(f'{first} - {second} - {third}')
