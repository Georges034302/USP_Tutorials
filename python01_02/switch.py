#!/bin/env python3

# Read HTTP code from STDIN
# Show info about it

code = int(input('HTTP Code: '))

match  code:
    case 200: print('Success')
    case 404: print('Page not Found')
    case 500: print('Server Error')
    case _: print('Unknow Code')
