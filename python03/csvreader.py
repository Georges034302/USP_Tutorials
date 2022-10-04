#!/bin/env python
#Read from CSV file and print the results as a list

import csv
import pprint as pp 

filename = input("Open file: ")

mydata = []

file = csv.DictReader(open(filename))

for line in file:
    mydata.append(line)

pp.pprint(mydata,indent=2,width=40)
