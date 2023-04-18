#!/bin/python3

name = "Tom"
balance = 250.5

#method 1
print(name+" has "+str(balance))

#method 2
print(name+" has ",balance)

#method 3
print("%s has %f"%(name,balance))
print("%s has %.3f"%(name,balance))
print("%20s has %f"%(name,balance))
print("%-20s has %f"%(name,balance))

#method 4
print("{} has {}".format(name,balance))
print("{} has {:.2f}".format(name,balance))
print("{:10} has {:20.2f}".format(name,balance))
print("{:<10} has {:<20.2f}".format(name,balance))
print("{:>10} has {:>20.2f}".format(name,balance))
print("{:*^10} has {:$^20.2f}".format(name,balance))

#method 5
print(f'{name} has {balance}')
print(f'{name:#^15} has {balance:$>20.4f}')
