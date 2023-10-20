#!/bin/python3
#Req: Determine the prime numbers in a random list 
#   - random list is between start, finish of size n 
#   - store the primes in a list
#   - show the list 
import random as ran 

def numbers(start,finish,size):
    return ran.sample(range(start,finish),size)

def is_prime(n):
    for e in range(2,n):
        if n%e == 0:
            return False 
    return True

def primes(mylist):
    prime_list = []
    for e in mylist:
        if is_prime(e):
            prime_list.append(e)
    return prime_list

def run():
    values = numbers(int(input('start: ')),int(input('finish: ')),int(input('size: ')))
    print(values)
    prime_list = primes(values)
    print(prime_list)

run()
