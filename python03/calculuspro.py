#Read integers until -1 from STDIN
#Determine the sum of all values
#Determine the min and max of all values
#Determine the average at 3 decimal points
import sys
n = int(input("N = "))

numbers = []
while n != -1:
    numbers.append(n)
    n = int(input("N = "))
    
print(f'Total = {sum(numbers)}')
print(f'Min = {min(numbers)}')
print(f'Max = {max(numbers)}')
print(f'Average = {sum(numbers)/len(numbers):.3f}')