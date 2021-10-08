#!/bin/env python3

#List is a collection of data. 
#A list is ordered, indexed, and changeable.
#List allows duplicate elements.

#Creating a list
mylist = ["Tom", 25, "has", 250, "dollars"]
list2 = list(["his","savings"])

#List length
print("List length = "+str(len(mylist)))

#Accessing list elements
print("First = "+mylist[0])
print("Last = "+ mylist[len(mylist)-1])
print("Sublist = "+str(mylist[2:4]))

#Moifying list elements
mylist[4] = "$"
print(mylist)

#Adding to a list 
mylist.insert(1,"Hanks")
print(mylist)
mylist.append("in")
print(mylist)

#Copying a list 
list1 = mylist.copy()
print(list1)

#Joining lists
mixedlist = list1 + list2 
print(mixedlist)

list3 = ["Bank", "AU"]
for e in list3:
    mixedlist.append(e)
print(mixedlist)

list4 = ["City", "Branch"]
mixedlist.extend(list4)
print(mixedlist)

#Reversing a list 
mixedlist.reverse()
print(mixedlist)
mixedlist.reverse()

#Deleting elements from a list 
mixedlist.remove("AU")
print(mixedlist)

mixedlist.pop()
print(mixedlist)

mixedlist.pop(2)
print(mixedlist)

del mixedlist[len(mixedlist)-1]
print(mixedlist)

mixedlist.clear()
print(mixedlist)

#Deleting a list
del mixedlist 
try:
    print(mixedlist)
except NameError:
    print("The list is not found!")

#Iterate a list 
for e in mylist:
    print(e,end=", ")
print()



































