#!/bin/env python3
#Define a function that reads any value from STDIN 
#Define a function that checks if a number is prime 
#Define a function that returns a list of primes numbers from a range (first,last)
#Define a function that saves the list of primes to a file  

def read(prompt):
    return input(prompt)

def isprime(n):
    for e in range(2,n):      #The any-pattern
        if n%e == 0:
            return False 
    return True 

def primelist(first,last):
    primes = []
    for e in range(first,last+1):   #The every-pattern
        if isprime(e):
            primes.append(e)
    return primes

def savetofile(mylist,filename):
    file = open(filename,'w+')
    for item in mylist:
        file.write(str(item))
        file.write("\n")
    file.close()

def main():
    first = int(read("First = "))
    last = int(read("Last = "))
    primes = primelist(first,last)
    print("List of primes between {} and {}:".format(first,last))
    print(primes)
    filename = read("Save to File: ")
    savetofile(primes,filename)
main()





