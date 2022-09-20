#!/bin/env python

name = "Tom"
balance = 150.5599

print("%s has %.2f"%(name,balance))
print("%20s has %10.2f"%(name,balance))
print("%-20s has %-10.2f"%(name,balance))


print("{} has {}".format(name,balance))
print("{} has {:.3f}".format(name,balance))
print("{:>10} has {:<15.3f}".format(name,balance))
print("{:^10} has {:^15.3f}".format(name,balance))
print("{:*^10} has {:$^15.3f}".format(name,balance))


print(f'{name} has {balance}')
print(f'{name:#^10} has {balance:$^10.3f}')

