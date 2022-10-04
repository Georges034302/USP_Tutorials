#!/bin/env python
#List is a collection of data
#List is ordered
#List is indexed
#List is changeable 
#List allows duplicates

mylist = ["Tom",30,101.55]          #creating a List
list2  = list(["Bank","Account"])   #creating a list using constructor

print(mylist)

print("First = ",mylist[0])         #Accessing element at position zero
length = len(mylist)                #return the list length or size
print("Last = ",mylist[length-1])   #Accessing the last element in the list

mylist.insert(2,"$")                #Inserting an element at position 2
print(mylist)
mylist.append("his")                #Adding element at the end of the list
print(mylist)
mylist.append(list2)
print(mylist)

print(mylist[2:])                   #slice from position 2 to the end 
print(mylist[2:5])                  #slice from position 2 to 5 (excluded)

mylist.pop()                        #remove the last element
print(mylist)  
mylist.pop(3)                       #remove element at index 3
print(mylist) 
mylist.remove("his")                #find an object and remove it
print(mylist) 

newlist = mylist + list2            #Joining two lists
print(newlist) 

del mylist                          #delete the list object
try:
    print(mylist)
except NameError:
    print("List does not exist")

print("List is fun")














