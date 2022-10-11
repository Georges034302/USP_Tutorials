#!/bin/env python 

# Read a string until * is entered
# Map the frequency of vowels to a dictionary
# Show the frequency of vowels
# save the frequencies to a file

import pprint as pp 

def read(prompt):
    return input(prompt)

# determine the frequency of a character in a string
def frequency(string, c):
    return string.lower().count(c)

# return a dictionary of vowel frequencies
def mapToDict(string):
    frequencies = {}
    for v in "aeiou":
        frequencies[v] = frequency(string,v)
    return frequencies

def show(dictionary):
    pp.pprint(dictionary,indent= 2, width= 20)

def save(dictionary,filename):
    file = open(filename, 'a+')
    for key in dictionary.keys():
        file.write(str(key)+"-"+str(dictionary[key]))
        file.write("\n")


def main():
    s = read("String: ")
    while s != "*":
        frequencies = mapToDict(s)
        save(frequencies,"data.txt")
        show(frequencies)
        s = read("String: ")
    print("- thank you")

main()











