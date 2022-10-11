#!/bin/env python

# Generate a random list with first, last, and size from STDIN 
# Calculate and return: sum, average, min, max of the list 
# Define the main() that shows all the values 

import random as r 

def read(prompt):
    return input(prompt)

def generate(first,last,size):
    return r.sample(range(first,last),size)

def calculate(*argv):
    s = sum(*argv)
    a = s/len(*argv)
    m = min(*argv)
    M = max(*argv)
    return s, a, m, M

def show(*argv):
    print(*argv)

def main():
    first = int(read("First = "))
    last = int(read("Last = "))
    size = int(read("Size = "))

    numbers = generate(first,last,size)
    show(numbers)
    s, a, m, M = calculate(numbers)

    print(f'Sum = {s}')
    print(f'Average = {a:.3f}')
    print(f'Min = {m}')
    print(f'Max = {M}')
main()










