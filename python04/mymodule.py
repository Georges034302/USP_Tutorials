#!/bin/env python3
#Define the read function 
#generate a random list of IDs (6 digits)
#generate a dynamic dictionary of students
#define a function to sort the dictionary
#define a function to update student name 
#define a function that deletes a student by key 
import random as ran 

def read(prompt):
    return input(prompt)

def ranlist(first,last,howmany):
    return ran.sample(range(first,last),howmany)

def dynamicdictionary(IDs):
    names = {}
    for key in IDs:
        names[key] = read("Name: ")
    return names

def sort(dictionary):
    for key in sorted(dictionary.keys()):
        print(" %s - %s "%(key,dictionary[key]))

def update(names,key,newname):
    names[key] = newname 

def delete(names, key):
    del names[key]
