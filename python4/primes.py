#!/bin/env python3
import random as ran

# Requirements:
# 1 - Generate a randon list ef integers
#       - size n from STDIN
#       - start value from STDIN
#       - end value from STDIN
# 2 - Check if a number is prime
# 3 - Determine the prime list from the random list
# 4 - Show both lists

# Objective 1
def random_list(start,end,n):
    return ran.sample(range(start,end+1),n)

# Objective 2
# To complete this objective, use the any-pattern
# def <noun>():
#   for <value> in <collection>:
#       if <condition is not true>
#           return False
#   return True
def is_prime(n):
    for e in range(2,n):
        if n%e == 0:
            return False
    return True

# Objective 3:
# To solve this objective, use the every pattern
# def <noun>():
#   <create temp collection>
#   for <value> in <original collection>
#       if <condition-value is true>
#           <add value to temp>
#   retun <temp collection>
def prime_list(numbers):
    primes = []
    for e in numbers:
        if is_prime(e):
            primes.append(e)
    return primes

# Objective 4
def run():
    start = int(input('start = '))
    end = int(input('end = '))
    n = int(input('size = '))
    numbers = random_list(start,end,n)
    primes = prime_list(numbers)
    print(numbers)
    print(primes)

run()



