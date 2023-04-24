#List is a collection of data (any data)
#List is ordered
#List is indexed
#List is changeable
#List allows duplicates

mylist = ["Tom", 30, 112.5]

length = len(mylist)
print(length)
print(mylist[0])
print(mylist[length -1])
print(mylist[1:])

mylist.append("$")  # adds a value to end of the list
print(mylist)

mylist.insert(2,"has") #injecting a value at index 2
print(mylist)

list2 = ["bank", "NSW"]
total = mylist + list2   #joining 2 lists
print(total)

total.remove("$")
print(total)

total.pop() #pops out element from end of the list
print(total)

total.pop(len(total)-2) #pops out element at index
print(total)

total.clear() #empty the list
print(total)

del total   #delete the object total completely
try:
    print(total)
except NameError:
    print("total has been deleted!")

print(mylist)