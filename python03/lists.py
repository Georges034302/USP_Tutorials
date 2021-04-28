#!/bin/env python3
#List is a collection of data
#A list is ordered, indexed, changeable
#A list allows duplications [duplicate elements]

mylist = ["Tom",25,"has",250.00,"$"]

print(mylist)
length = len(mylist) #length of the list

#Accessing the list elements
print("First: "+mylist[0])
print("Last: "+mylist[length-1])
print("First three: "+str(mylist[:3]))
print("Elements from 2 to last: "+str(mylist[2:]))
print("Elements from index 1 to 4: "+str(mylist[1:5]))

#Updating a list
mylist[4] = "dollars" #updating a value in a list
mylist.insert(1,"Hanks") #inserting a value at an index
mylist.append("in") #adding a value at the end of the list
print(mylist)

#copying a list
list1 = mylist.copy()
print(list1)

#joining 2 lists
list2 = list(["his","savings"]) #creating a list using the constructor
mixedlist = list1 + list2
print(mixedlist)
list3 = ["CBA","Account"]
mixedlist.extend(list3)
print(mixedlist)

#reverse a list
mixedlist.reverse()
print(mixedlist)

#Delete elements from the list
mixedlist.remove("Account") #removed Account

mixedlist.pop() #delete last element
mixedlist.pop() #delete last element
mixedlist.pop(4) #delete element at index 4
print(mixedlist)

del mixedlist[0] #delete element at index using the del function
print(mixedlist)

mixedlist.clear() #clears all elements in the list
print(mixedlist)

#delete a list in python3
del mixedlist #deletes the object mixedlist
try:
    print(mixedlist)
except NameError:
    print("mixedlist does not exist")

#Iterating a list 
for e in mylist:
    print(e, end=" ")
print()

itlist = iter(mylist)
for i in itlist:
    print(i, end=" ")
print()

for e in enumerate(mylist):
    print(e, end=" ")
print()


















