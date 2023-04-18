#!/bin/python3
# A dry spell is the number of days with zero rain
# Determine the maximum dry spell
# Read rain until -1 and calculate the maximum dry days

import sys
rain = int(input("Rain: "))

maximum = -sys.maxsize

count = 0

while rain != -1:
    if rain == 0:
        count +=1 
    else:
        maximum = max(maximum,count)
        count = 0
    rain = int(input("Rain: "))

maximum = max(maximum,count)    
print(f'Longest dry spell = {maximum}')