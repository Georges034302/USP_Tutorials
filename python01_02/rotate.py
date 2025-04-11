#!/bin/env python3

# Rotate the bar | 360 degrees
import time
bar = '|/-\\'
index = 0

while True:
    print(f'\r{bar[index]}',end="")
    index = (index+1) % len(bar)
    time.sleep(0.1)

