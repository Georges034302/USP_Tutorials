#!/bin/env python3
#read a csv file (filename from argument)
#convert the csv data to dictionary 

import csv 
import sys
import pprint 

filename = sys.argv[1]
fin = csv.DictReader(open(filename))           #open the filename

mylist = []

for line in fin:
    mylist.append(line)

pp = pprint.PrettyPrinter(indent=2,width=40)

pp.pprint(mylist)



