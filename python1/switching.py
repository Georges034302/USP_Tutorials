#!/bin/python3
# Req: Read HTTP error code from STDIN
# Provide error message to the user 

code = int(input('HTTP code: '))

match code:
    case 404: print('Page not found')
    case 200: print('Success')
    case 300: print('Multiple Choices')
    case 500: print('Internal Server Error')
    case _: print('Unknown code!!!!')
