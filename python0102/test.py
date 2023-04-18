#!/bin/python3

import sys

x = int(sys.argv[1])

if x > 0 :
    if x > 10:
        print (str(x) + " > 10")
    elif x < 10:
        print (str(x) +" < 10")
    else:
        print(str(x)+" == 10")
else:
    print(str(x)+" < 0")