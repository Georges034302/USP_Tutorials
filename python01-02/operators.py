#!/bin/env python3 

a = 2
b = 3

print("a + b = ",(a+b))
print("a - b = ",(a-b))
print("a * b = ",(a*b))
print("a / b = ",(a/b))
print("a / b = {:.3f}".format(a/b))
print(f'a / b = {(a/b):.2f}')
print("a / b = %.4f"%(a/b))

print("a power b = ",a**b)
print(f'a power b = {pow(a,b)}')

a += 2  #a = a + 2
b += 3  #b = b + 3

print(a+b)

a *= 2  # a = a * 2
b /= 2  # b = b/2

print(a)
print(b)
print(a - b)

print(a%b)

a %= 3  # a = a % 3
print(a)


