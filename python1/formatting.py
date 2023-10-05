#!/bin/python3
# Tom has $<the balance> formatted in different ways
name = 'Tom'
balance = 112.365

# Method 1:
print(name,' has $',balance)

# Method 2:
print(name+' has $'+str(balance))

# Method 3:
print('%s has $%.2f'%(name,balance))
print('%10s has $%12.2f'%(name,balance))
print('%-10s has $%-12.2f'%(name,balance))

# Method 4:
print('{} has ${}'.format(name,balance))
print('{:8} has ${:11.4f}'.format(name,balance))
print('{:>8} has ${:11.4f}'.format(name,balance))
print('{:^8} has ${:11.4f}'.format(name,balance))
print('{:*^8} has ${:$^15.4f}'.format(name,balance))

# Method 5:
print(f'{name} has ${balance}')
print(f'{name:10} has ${balance:12.2f}')
print(f'{name:10} has ${balance:<12.2f}')
print(f'{name:@^10} has ${balance:$^12.2f}')







