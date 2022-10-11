#!/bin/env python

# 1- Function with a return value 
#       def <function-name> (<parameters>):
#           <code-block>
#           return <value>

# 2- Function with no return value (procedures - actions)
#       def <function-name> (<parameters>):
#           <code-block>
#   

# 3- Function that returns multiple values
#       def <function-name> (<parameters>):
#           <code-block>
#           return <value 1>, <value 2> ....

numbers = list(range(1,10));    #generating a sequential list

#function definition - *argv represents a list (or collection)
def show(*argv):
    print(*argv)
    print("Thank you")

show(numbers)


# function that returns a value
def total(a,b,c):
    return a+b-c

print(total(4,8,6))


# function that returns multiple values
def valuesUpdate(a,b,c):
    a += 2
    b *= a
    c += a+b
    return a,b,c

m,n,p = valuesUpdate(4,3,2)
print(f'{m} - {n} - {p}')






