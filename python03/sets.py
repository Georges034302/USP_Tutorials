#Set is a collection of data (any data)
#Set is unordered
#Set is not indexed 
#Set is changeable
#Set is unique, it does not allow duplicates

set1 = {"AWS", "Restart", "MEL", 11, 2023}
print(set1)

set1.add("AWS") #AWS is not added, because sets are unique
print(set1)

set1.add("Python")
print(set1)

set1.update(["Feb",28])
print(set1)

set1.remove(28)
print(set1)

set1.discard("Feb")
print(set1)

set1.pop()  #remove the element that happened to be last this time
print(set1)

set2 = {"Cohort", 22}
newset = set1.union(set2)
print(newset)

del newset
try:
    print(newset)
except NameError:
    print("newset does not exist!")

print(set1)