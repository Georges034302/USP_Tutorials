#!/bin/env python3

# Read rain until -1
# Determine and show the longest dry spell
import sys 

maximum = - sys.maxsize
rain = int(input('rain: '))
count = 0

while rain != -1:
    if rain == 0:
        count +=1
    else:
        maximum = max(maximum , count)
        count = 0
    rain = int(input('rain: '))
if count > maximum:
    maximum = count
print(f'Logest dry spell = {maximum}')
