#!/bin/env python3
import csv
import pandas as pd
import json

# define a function to return the number of vowels in a string
# define a function to return frequency of every vowel formatted as:
# vowel --> frequency
# define a function to read a string until * and show the frequencies of the vowels
# store the frequencies in a a text file and read it out
# store the frequencies in a csv file and read it out
# store the frequencies in a json file and read it out

def frequency(c,string):
    return string.count(c)

def frequencies(string):
    data = {} # to store the frequency of each vowel
    for c in 'aeiou': # c is the key in the dictionary
        data[c] = frequency(c,string) # data[c] is the value in the dictionary
    return data

def print_frequencies(data):
    for key in data.keys(): # iterate over the keys in the dictionary
        print(f"{key} --> {data[key]}") # print the frequency of each vowel

def save_to_txt(structure):
    handler = open('vowels.txt', 'w') # open the file in write mode
    for data in structure: # iterate over the data
        for key in data.keys(): # iterate over the keys in the dictionary
            handler.write(f"{key} --> {data[key]}\n")
    handler.close() # close the file

def read_from_txt():
    handler = open('vowels.txt', 'r') # open the file in read mode
    content = handler.read() # read the file
    print(content) # print the data
    handler.close() # close the file

def save_to_csv(structure):
    handler = open('vowels.csv', 'w', newline='') # open the file in write mode
    write = csv.writer(handler) # create a csv writer object
    write.writerow(['Vowel', 'Frequency']) # write the header
    for data in structure:
        for key in data.keys():
            write.writerow([key, data[key]])
    handler.close() # close the file

def read_from_csv():
    df = pd.read_csv('vowels.csv') # read the csv file
    print(df) # print the data

def save_to_json(structure):
    handler = open('vowels.json', 'w') # open the file in write mode
    json.dump(structure, handler,indent=2) # dump the data to the file
    handler.close() # close the file

def read_from_json():
    handler = open('vowels.json', 'r') # open the file in read mode
    content = json.load(handler) # load the data from the file
    print(json.dumps(content,indent=4)) # print the data
    handler.close() # close the file

def main():
    structure = [] # to store the dictionary of each string
    s = input('string: ')
    while s != '*':
        data = frequencies(s.lower()) # frequencies dictionary
        structure.append(data)
        save_to_txt(structure)
        save_to_csv(structure)
        save_to_json(structure)
        #print_frequencies(data) # print the frequencies
        s = input('string: ')
    read_from_txt() # read the file
    read_from_csv() # read the csv file
    read_from_json() # read the json file
main()