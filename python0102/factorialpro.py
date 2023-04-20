#Read integers until -1 from STDIN
#Determine and show the factorial of all values

import math as m

n = int(input("N = "))

while n != -1:   
    print(f'N = {n} - Factorial(N) = {m.factorial(n)}')
    n = int(input("N = "))