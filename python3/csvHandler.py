#!/bin/python3
import csv 
import pandas as pa
import json 
import random as ran 

def random_ID():
    return ran.randint(100000,999999)

def random_mark():
    return ran.randint(25,100)

def grade(mark):
    if mark >= 85:
        g = 'HD'
    elif mark >= 75:
        g = 'D'
    elif mark >= 65:
        g = 'C'
    elif mark >= 50:
        g = 'P'
    else:
        g = 'Z'
    return g

def write_to_csv(filename):
    with open(filename,'a',newline='') as handler:
        csv_writer = csv.writer(handler)
        name = input('Student name: ')
        id = random_ID()
        mark = random_mark()
        g = grade(mark)
        row = [id,name,mark,g]
        csv_writer.writerow(row)

write_to_csv('students.csv')

def read(filename):
    data = []
    with open(filename,'r') as handler:
        csv_obj = csv.DictReader(handler)
        for row in csv_obj:
            data.append(row)
    return data

def read_pandas(filename):
    data = pa.read_csv(filename)
    print(data)

read_pandas('students.csv')

def save_to_json(filename,data):
    handler = open(filename,'w')
    handler.write(json.dumps(data,indent=4))
    handler.close()
data = read('students.csv')
save_to_json('students.json',data)



