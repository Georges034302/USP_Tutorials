#!/bin/python3
# dictionary is indexed by unique key 
# dictionary is unordered
# dictionary allows only duplicate values
import pprint as pp
data = {'name':'Tom',
        'age':30,
        'mark':77,
        'grade':'D'
    }
print(data['grade'])

del data['grade']
print(data)
pp.pprint(data,width=20)

data['mark'] = 80
pp.pprint(data,width=20)

data['role'] = 'student'
pp.pprint(data,width=20)


other = {'age': 44,
         'grade':'D'
         }
data.update(other)
pp.pprint(data,width=20)


