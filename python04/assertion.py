
import unittest as test
    
def div(a,b):
    test.validate_input(a)
    test.validate_input(b)
    test.validate_b_not_zero(b)
    return int(a)/int(b)

a = input("a = ")
b = input("b = ")

print(div(a,b))