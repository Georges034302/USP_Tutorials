#!/bin/env python3

name = 'Tom'
balance = 25.5
# I want to always display:
# name has balance

# Method 1: using concatunation
print(name+" has "+str(balance))

# Method 2: using comma 
print(name,'has',balance)

# Method 3: using format modes 
print('%s has %f '%(name,balance))
print('%s has %.3f '%(name,balance))
print('%10s has %15.3f '%(name,balance))
print('%-10s has %-15.3f '%(name,balance))

# Method 4: using the format function
print('{} has {}'.format(name,balance))
print('{} has {:.4f}'.format(name,balance))
print('{:10} has {:15.4f}'.format(name,balance))
print('{:>10} has {:15.4f}'.format(name,balance))
print('{:^10} has {:^15.4f}'.format(name,balance))
print('{:*^10} has {:$^15.4f}'.format(name,balance))

# Method 5: using f-string
print(f'{name} has {balance}')
print(f'{name} has {balance:.4f}')
print(f'{name:10} has {balance:15.4f}')
print(f'{name:>10} has {balance:15.4f}')
print(f'{name:^10} has {balance:^15.4f}')
print(f'{name:*^10} has {balance:$^15.4f}')










