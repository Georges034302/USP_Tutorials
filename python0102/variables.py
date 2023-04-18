#!/bin/python3

a = 2
f = 3.5
b = True
s = "Hello"

print(type(a))
print(type(f))
# f=4
# print(type(f))
print(type(b))
print(type(s))

x = a + 1

print(x)
x += 1 # x = x +1
print(x)

y = f / 2
print(y)

y /= 2 # y = y /2
print(y)

m = a * 2
print(m)

m *= 3 # m = m *3
print(m)

z = m + 1
z %= 5 # z = z % 5
print(z)

#print(s+z) # this will not work because z is int
print(s + str(z))
print(s + str(b))

print(a+f) # adding int to float
print(a + b)


# print(a +int(s)) cannot convert str to int