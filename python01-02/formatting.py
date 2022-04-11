#!/bin/env python3 

name = "Tom"
balance = 75.5

print(name+" has $"+str(balance))
print(name," has $",balance)

print("%s has $%f"%(name,balance))
print("%10s has $%15.2f"%(name,balance))
print("%-10s has $%15.2f"%(name,balance))

print("{} has ${}".format(name,balance))
print("{} has ${:.3f}".format(name,balance))
print("{:10} has ${:15.3f}".format(name,balance))
print("{:10} has ${:<15.3f}".format(name,balance))
print("{:^10} has ${:<15.3f}".format(name,balance))
print("{:*^10} has ${:$<15.3f}".format(name,balance))

print(f'{name:10} has ${balance:.3f}')
print(f'{name:>10} has ${balance:20.3f}')
print(f'{name:>10} has ${balance:^20.3f}')
