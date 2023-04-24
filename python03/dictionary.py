#Dictionary is a collection of data organized as key-value
#Dictionary is unordered 
#Dictionary is indexed
#Dictionary is changeable
#Dictionary is unique (unique keys)

import pprint as pp

dict1 = {
    "name":"Tom",
    "age": 30,
    "role":"admin",
    "active":True
}

print(dict1)
print(dict1["role"])
pp.pprint(dict1,width=40)

del dict1["active"]
pp.pprint(dict1,width=40)

dict1["balance"] = 112    # add a new key-value association
pp.pprint(dict1,width=40)

dict1["age"] = 112    #update a value by key
pp.pprint(dict1,width=40)

del dict1
try:
    pp.pprint(dict1,width=40)
except NameError:
    print("dictionary is deleted")
    
