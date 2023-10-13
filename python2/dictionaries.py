#!/bin/python3
# Dictionary is a collection of data
# stored as: key --> value 
# Dictionary is not ordered
# Dictionary is not indexed
# Dictionary keys are unique 
# Dictionary values can be duplicates
# Dictionary is changeable
import pprint as pp 
data = {
    'name':'Lana',
    'age': 29,
    'role': 'HR'
}

print(data['role'])
print(len(data))
print(data.keys())
print(data.values())

data['salary'] = 100000
print(data)
pp.pprint(data,indent=4,width=40)

data['role'] = 'admin'
pp.pprint(data,indent=4,width=40)

data.update({'ID':999,'Location': 'Syd'})
pp.pprint(data,indent=4,width=40)

del data['Location']
pp.pprint(data,indent=4,width=40)



