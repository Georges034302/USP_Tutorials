#!/bin/python3
import sys

length = len(sys.argv)

if length == 1:
    print("Script name: "+sys.argv[0])
elif length == 2:
    print("Script has one arg: "+sys.argv[1])
else:
    print("Script args: "+str(sys.argv))