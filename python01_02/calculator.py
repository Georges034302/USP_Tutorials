#!/bin/env python3
# Read three arguments as following:
# a op b
# a: first number
# op: operator
# b: second number
# print the result of the operation a op b
# op: +, -, *, /
import sys

result = 0
a = sys.argv[1]
b = sys.argv[3]
op = sys.argv[2]

match op:
    case '+':
        result = int(a) + int(b)
    case '-':
        result = int(a) - int(b)
    case '*':
        result = int(a) * int(b)
    case '/':
        result = int(a) / int(b)
    case _:
        print("Invalid operator")
        sys.exit(1)
print(f"{a} {op} {b} = {result}")