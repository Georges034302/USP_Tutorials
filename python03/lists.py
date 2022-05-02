#!/bin/env python3
# List is a collection of data of any type 
# List is ordered
# List is indexed 
# List is changeable
# List allows duplicates

mylist = ["Tom", 30, 25.5, True]                #creating a list 
rangelist = list(range(1,11))                   #creating a list 

print(mylist)                                   #printing a list
print(rangelist)                                #printing a list

length = len(mylist)                            #determine list length
print("Length = %d"%(length))

print("First = ",mylist[0])                     #reading first element
print("Last = {}".format(mylist[length-1]))     #reading last element
print("Slice(0 to 2) = ",mylist[0:3])           #slicing elements at index 0, 1 , 2
print(f'Slice (2 to the end) = {mylist[2:]}')   #slicing elements from 2 to the end
print(mylist[-3:-1])                            #reverse readin from -3 to -1

mylist.insert(1,"Smith")                        #inserting an element at index
print(mylist)

mylist.append(False)                            #adding element at the end
print(mylist)

mylist.remove(25.5)                             #finds and remove a value
print(mylist)

mylist.pop()                                    #discard the last element
print(mylist)

mylist.pop(1)                                   #delete element by index
print(mylist)

newlist = mylist + rangelist                    #joining lists
print(newlist)

newlist.reverse()                               #reverse a list
print(newlist)

newlist.clear()                                 #empty a list
print(newlist)

del mylist                                      #delete a list

try:
    print(mylist)
except NameError:
    print("mylist does not exist!")












