#Convert a number from STDIN into 8-bits binary representation
# n/2 --> /2 /2 ---> 0 
n = int(input("N = "))

list1 = []
zeros = [0,0,0,0,0,0,0,0]

while n > 0:
    list1.append(int(n%2))
    n = int(n/2)

reverse = list(reversed(list1))

binary = zeros[len(reverse):len(zeros)]+reverse

print(binary)