#!/bin/env python3
#List is a collection of DATA. A list is  ordered, indexed and chanegable
#List allows duplicate elements

mylist = ["Tom",25,"has",250,"dollars"]
print(mylist)
print("List length = "+str(len(mylist)))

print(">>> 1- Accessing list elements")
print(mylist[2])
print(mylist[len(mylist)-1])
print(mylist[-3])
print(mylist[2:])
print(mylist[:3])
print(mylist[1:4])
print(mylist[-4:-1])

print(">>> 2- updating a list")
mylist[4] = "$"
print(mylist)

mylist.insert(1,"Hanks")
print(mylist)

mylist.append("in")
print(mylist)

print(">>> 3- copying a list")
list1 = mylist.copy()
print(list1)


print(">>> 4- joining 2 lists")
list2 = list(["his","savings"])
mixedlist = list1 + list2
print(mixedlist)

list3 = ["Bank","AU"]
for x in list3:
    mixedlist.append(x)
print(mixedlist)

list4 = ["City", "Branch"]
mixedlist.extend(list4)
print(mixedlist)

print(">>> 5- reverse a list")
mixedlist.reverse()
print(mixedlist)


print(">>> 6- deleting elements from a list")
mixedlist.remove("Branch")
print(mixedlist)

mixedlist.pop(2)
print(mixedlist)

mixedlist.pop()
print(mixedlist)

del mixedlist[len(mixedlist)-1]
print(mixedlist)

mixedlist.clear()
print(mixedlist)

print(">>> 7- deleting a list")
del mixedlist
try:
    print(mixedlist)
except NameError:
    print("mixedlist has been deleted!!!")

print(">>> 8- iterate a list")
for x in mylist:
    print(x, end=", ")
print()

itlist = iter(mylist)
for x in itlist:
    print(x, end=", ")
print()

for x in enumerate(mylist):
    print(x)































































