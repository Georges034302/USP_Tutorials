#!/bin/env python3

# Read day and month from STDIN
# Determine the number of days from Jan 1, until the day
# HINT: no leap year

days = [31,28,31,30,31,30,31,31,30,31,30,31]

day = int(input('Day: '))
month = int(input('Month: '))

i = 0
total = 0

while i < month-1:
    total += days[i]
    i+=1

total += day 

print(f'Total days = {total}')