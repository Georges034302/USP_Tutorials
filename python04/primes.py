#!/bin/env python 

# Generate a random list with first, last, size from STDIN
# Determine and show the prime numbers in this list
# Save the prime numbers to a file  

import random as r 

def read(prompt):
    return input(prompt)

def generate(first,last,size):
    return r.sample(range(first,last),size)

def show(*argv):
    print(*argv)

def isPrime(n):
    for e in range(2,n):
        if( n % e == 0):
            return False 
    return True

def primesList(numbers):
    primes = []
    for n in numbers:
        if(isPrime(n)):
            primes.append(n) 
    return primes

def save(primes,filename):
    file = open(filename, 'a+')
    for n in primes:
        file.write(str(n)+", ")

def main():
    first = int(read("First = "))
    last = int(read("Last = "))
    size = int(read("Size = "))

    numbers = generate(first,last,size)
    show(numbers)
    primes = primesList(numbers)
    save(primes,"primes.txt")
    show(primes)
    
main()







