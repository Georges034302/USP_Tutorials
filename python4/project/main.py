#!/usr/bin/env python3
import util as u

def circleops():
    r = u.read("Radius")
    if r.isdigit():
        p, a, sa, sv = u.circle(r)
        print("Perimeter = %.2f "% p)
        print("Area = %.2f"% a)
        print("Sphere area = %.3f"% sa)
        print("Sphere volume = %.4f"% sv)
    else:
        print("Input TypeError "+r)

def listops():
    list = u.randomlist(1,10,5)
    mean, var, stdv, sum = u.liststats(list)  
    print(list)
    print("Sum = %.2f "% sum)
    print("Mean = %.2f "% mean)
    print("Variance = %.3f"% var)
    print("Standard Dev = %.4f"% stdv)

def dictops():
    names = u.createdict()
    u.printdict(names)
    key = int(u.read("update by key"))
    value = u.read("new value")
    u.update(names,key,value)
    u.printdict(names)
    key = int(u.read("delete by key"))
    u.delete(names,key)
    u.printdict(names)

def main():
    print("\nRunning util functions::")
    print("-------------------------")
    print("\n>>>Circle Ops::")
    circleops()
    print("\n>>>List Ops::")
    listops()
    print("\n>>>Dictionary Ops::")
    dictops()
    print("-------------------------\n")

main() #running the main method of the project - entry point



