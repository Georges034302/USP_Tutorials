#!/bin/env python3
import math as m

# Method can be procedure or function

# Procedure:
# Procedure is a method that does an action
# Procedure then is a verb
# Procedure does not return a value
# Syntax: 
# def <verb> (args):
#   <code - action>


# Function:
# Function is a method that returns a value
# Function is a noun
# Function can be stored in a variable
# Syntax:
# def <noun>(args):
#   <code>
#   return <value(s)>


# Requirements:
# 1- Read a positive integer n from STDIN
# 2- Calculate the factorial of n
# 3- Calculate the: perimeter, area, volume, (circle/sphere of radius n)
# 4- Show the collatz table of n

# Objective 1
n = int(input("N = "))

# Objective 2:
def factorial(n):
    f = 1
    for e in range(2,n+1):
        f *= e 
    return f
print(f'Factorial({n}) = {factorial(n)}') # invoking the function

# Objective 3:
def geometry_values(n):
    p = 2*m.pi*n
    a = m.pi*pow(n,2)
    v = (4/3)*m.pi*m.pow(n,3)
    return p, a, v

p,a,v = geometry_values(n) # Invoke the function
print(f'Perimeter = {p:.2f}; Area = {a:.3f}; Volume = {v:.2f}')

# Objective 4:
# F(n) = n/2 if n is even or 3n+1 if n is odd
def show_collatz(n):
    while n > 1:
        if n%2 == 0:
            print(f'{n:4} - {int(n/2):4}')
            n = int(n/2)
        else:
            print(f'{n:4} - {3*n+1:4}')
            n = 3*n +1

show_collatz(n)
