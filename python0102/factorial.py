#Read integers until -1 from STDIN
#Determine and show the factorial of all values

n = int(input("N = "))

while n != -1:
    f = 1
    for e in range(1,n+1):
        f *= e
    print(f'N = {n} - Factorial(N) = {f}')
    n = int(input("N = "))