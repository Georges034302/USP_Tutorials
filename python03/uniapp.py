#!/bin/env python3

# Register n students in your uni db (n from STDIN)
# every student has 3-digit random ID (key)
# every student has a name and age
# ID => {name, age}
# students = {
#     ID1:{name1,age1},
#     ID2:{name2,age2},
#     ....
# }
import random as ran 
import pprint as pp 

n = int(input('n = '))

# list of 3-digit IDS
ids = ran.sample(range(100,1000), n)  

# students dictionary
students = {} 

for ID in ids:
    print(f'Student: {ID}')
    name = input('name: ')
    age = input('age: ')
    student = {}
    student['name'] = name
    student['age'] = age
    students[ID] = student 

pp.pprint(students,indent=2,width=20)





