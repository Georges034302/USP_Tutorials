#!/bin/env python3

#def <function-name>(<arguments>):
#   <code>

def read():
    return input("Enter your name: ")


def show(name):
    print("Welcome ",name)

def main():
    name = read()
    show(name)

main()

