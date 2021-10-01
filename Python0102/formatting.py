#!/bin/env python3

name = "Tom"
savings = 250
loan = 100.50

#Method 1:
print(name+" has: $"+str(savings)+" and owes: $"+str(loan))

#Method 2:
print("%s has: $%d and owes: $%f"%(name,savings,loan))
print("%s has: $%d and owes: $%.2f"%(name,savings,loan))
print("%s has: $%.3f and owes: $%.2f"%(name,savings,loan))
print("%10s has: $%15.3f and owes: $%12.2f"%(name,savings,loan))
print("%-10s has: $%-15.3f and owes: $%-12.2f"%(name,savings,loan))

#Method 3:
print("{} has: ${} and owes: ${}".format(name,savings,loan))
print("{:<10} has: ${:<15.2f} and owes: ${:<12.3f}".format(name,savings,loan))
print("{:>10} has: ${:>15.2f} and owes: ${:>12.3f}".format(name,savings,loan))
print("{:^10} has: ${:^15.2f} and owes: ${:^12.3f}".format(name,savings,loan))
print("{2:<10} has: ${0:<15} and owes: ${1:<12.3f}".format(name,savings,loan))
print("{:*^10} has: ${:=^15.2f} and owes: ${:-^12.3f}".format(name,savings,loan))
