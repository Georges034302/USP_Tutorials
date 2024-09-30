#!/bin/env python3

# Read a day and a month from STDIN
# Determine the total days from January first until the day

day = int(input('day: '))
month = int(input('month: '))

days = [31,28,31,30,31,30,31,31,30,31,30,31]

i = 0
total = 0

while i < month-1:
    total += days[i]
    i += 1
total += day 
print(f'Total days = {total}')
