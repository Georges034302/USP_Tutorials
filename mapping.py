import csv
import pprint as pp
import sys

#filename = input("Enter filename: ")
filename = sys.argv[1]

file = csv.DictReader(open(filename))

dictionary = [] #empty

for line in file:
    dictionary.append(line)

pp.pprint(dictionary)

