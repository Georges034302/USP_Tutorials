#!/bin/env python3

# Requirements:
# Read a string from STDIN until *
# Show the frequency of vowels formatted as:
#   vowel ---> frequency

def frequency(c,string):
    return string.lower().count(c)

def frequencies(string):
    data = {}
    for c in "aeiou":
        data[c] = frequency(c,string)
    return data

def show(data):
    for key in data.keys():
        print(f'{key} ---> {data[key]}')

def run():
    s = input('String: ')
    while s != '*':
        data = frequencies(s)
        show(data)
        s = input('String: ')

run()