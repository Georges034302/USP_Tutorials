#!/bin/python3
#Req: Read a string until *
#   Determine the frequncy of vowels in a string 
#   Store the results into a data structure
#   Save the structure into a text file  
#   Read the text file and show the results 
import pprint as pp 

def frequency(c, s):
    return s.lower().count(c)

def frequencies(s):
    data = {}
    for c in "aeiou":
        data[c] = frequency(c,s)
    return data  

def show(data):
    pp.pprint(data,indent=2,width=20)

def save_to_text(structure):
    handler = open('data.txt','a')
    for data in structure:
        for key in data.keys():
            handler.write(f'{key} --> {data[key]}')
            handler.write('\n')
    handler.close()

def read_from_text():
    handler = open('data.txt','r')
    content = handler.read() 
    print(content)
    handler.close()

def run():
    s = input('String: ')
    structure = []
    while s != '*':
        data = frequencies(s) 
        structure.append(data)         
        s = input('String: ')
    save_to_text(structure)
    read_from_text()

run()

