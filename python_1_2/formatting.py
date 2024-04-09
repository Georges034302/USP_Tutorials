#!/bin/env python3

name = 'Tom'
balance = 45.5

# Display: name has balance

# Method 1: convert all arguments to string using str
print(name+' has '+str(balance))

# Method 2: print arguments next to each other separated by comma
print(name,' has ',balance)

# Method 3: using formatting modes
print('%s has %f'%(name,balance))
print('%15s has %.3f'%(name,balance))
print('%-15s has %.3f'%(name,balance))

# Method 4: using the string format function
print('{} has {}'.format(name,balance))
print('{:20} has {:.4f}'.format(name,balance))
print('{:>20} has {:.4f}'.format(name,balance))
print('{:^20} has {:10.4f}'.format(name,balance))
print('{:*^20} has {:$^15.4f}'.format(name,balance))

# Method 5: f-string
print(f'{name} has {balance}')
print(f'{name:20} has {balance:.4f}')
print(f'{name:>20} has {balance:.4f}')
print(f'{name:^20} has {balance:10.4f}')
print(f'{name:*^20} has {balance:$^15.4f}')






