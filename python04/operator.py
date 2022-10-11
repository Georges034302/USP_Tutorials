#!/bin/env python

import utils as u 

def main():
    first = int(u.read("First = "))
    last = int(u.read("Last = "))
    size = int(u.read("Size = "))

    numbers = u.generate(first,last,size)
    u.show(numbers)

    target = int(u.read("Target = "))
    found = u.find(target,numbers)
    if found:
        print(f'{target} exists in the list')
    else:
        print(f'{target} does not exist')

main()
