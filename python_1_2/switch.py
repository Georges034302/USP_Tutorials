#!/bin/env python3

direction = input('Direction(N/S/E/W): ')

match direction:
    case 'N': print('Going North on the bridge')
    case 'S': print('Going South on M5')
    case 'E': print('Going East on M1')
    case 'W': print('Going West on M4')
    case _: print('Incorrect Direction')
