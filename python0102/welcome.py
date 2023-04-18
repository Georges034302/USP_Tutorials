#!/bin/python3
# Read a name from STDIN and compare it to Tom or print goodbye

name = input("Name: ")

if name.lower() == "Tom".lower():
    print("Welcome "+name)
else:
    print("Goodbye!")