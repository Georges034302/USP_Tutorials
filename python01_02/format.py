#!/bin/env python3

name = 'Tom'
balance = 125.8
# name has balance 

print(name,' has ',balance) # printing 3 items  next to each other

print(name+' has '+str(balance)) # concatunating string
print('%s has %f'%(name,balance))
print('%s has %.3f'%(name,balance))
print('%10s has %12.3f'%(name,balance))
print('%-10s has %12.3f'%(name,balance))

print('{} has {}'.format(name,balance))
print('{} has {:.3f}'.format(name,balance))
print('{} has {:15.3f}'.format(name,balance))
print('{} has {:>15.3f}'.format(name,balance))
print('{} has {:$^15.3f}'.format(name,balance))
print('{} has {:%>15.3f}'.format(name,balance))

print(f'{name} has {balance}')
print(f'{name} has {balance:12.4f}')
print(f'{name} has {balance:^12.4f}')
print(f'{name} has {balance:#^12.4f}')





