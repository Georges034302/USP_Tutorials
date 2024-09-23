#!/bin/env python3

# Read destination and show the road

d = input('Destination(N/S/E/W): ')

match(d):
    case 'N': print('Go north on M1')
    case 'S': print('Go south on M5')
    case 'E': print('Go East on M8')
    case 'W': print('Go west on M4')
    case _: print('Unknown direction')
