#Tuple is a collection of any data
#Tuple is ordered
#Tuple is indexed
#Tuple is unchangeable
#Tuple allows duplicates

tuple1 = ("Tom",30,112.5)

print(tuple1)
print(tuple1[len(tuple1)-1])
print(tuple1[0])

tuple2 = ("$", "bank")

newtuple = tuple1 + tuple2

print(newtuple)

del newtuple
try:
    print(newtuple)
except NameError:
    print("newtuple does not exist!")

tuple1 = tuple2
print(tuple1)