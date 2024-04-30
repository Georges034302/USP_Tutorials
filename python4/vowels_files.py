#!/bin/env python3
import csv 
import pandas
import json 

# Requirements:
# Read a string from STDIN until *
# Show the frequency of vowels formatted as:
#   vowel ---> frequency
# Save the data to text file
# Save the data to CSV file
# Save the data to JSON file
# Read from files and show the data (text,csv,json)

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

def save_to_txt(structure):
    handler = open('data.txt','w')
    for data in structure:
        for key in data.keys():
            handler.write(f'{key} ---> {data[key]}')
            handler.write('\n')
    handler.close()

def read_from_txt():
    handler = open('data.txt','r')
    content = handler.read()
    print(content)
    handler.close()

def save_to_csv(structure):
    header = ['Vowel','Frequency']
    with open('data.csv','w') as handler:
        writer = csv.writer(handler)
        writer.writerow(header)
        for data in structure:
            for key in data.keys():
                writer.writerow([key,data[key]])
    # handler.close()

def read_from_csv():
    data_frame = pandas.read_csv('data.csv')
    print(data_frame)

def save_to_json(structure):
    handler = open('data.json','w')
    json.dump(structure,handler,indent=2)
    handler.close()

def read_from_json():
    handler = open('data.json','r')
    content = json.load(handler)
    print(json.dumps(content,indent=4))
    handler.close()

def run():
    structure = []
    s = input('String: ')
    while s != '*':
        data = frequencies(s)
        structure.append(data)
        save_to_txt(structure)
        save_to_csv(structure)
        save_to_json(structure)
        #show(data)
        s = input('String: ')
    read_from_txt()
    read_from_csv()
    read_from_json()
run()