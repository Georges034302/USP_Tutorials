#!/bin/env python3

# Read rain until -1
# Show the longest dry spell
# NOTE: dry spell is the number of days with no rain
import sys
max_value = -sys.maxsize

rain = int(input('rain: '))
count = 0

while rain != -1:
    if rain == 0:
        count += 1 
    else:
        max_value = max(max_value, count)
        count = 0
    rain = int(input('rain: '))
max_value = max(max_value,count)

print(f'Longest dry spell = {max_value}')

