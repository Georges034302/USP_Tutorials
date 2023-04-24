#!/bin/python3
import sys
import re

students= {}
fin = open(sys.argv[1])

for line in fin:
	line = line.rstrip('\n')
	students = re.split(';',line)
	print (students)


