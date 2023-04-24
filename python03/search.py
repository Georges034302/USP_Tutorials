#Read the demo.txt file
#Search and replace patterns in the file
import re
choice = input("Choice (s/x): ")

while choice != "x":
    f = open("demo.txt","r")
    regex = input("Pattern: ")
    replacement = input("Replacement: ")
    for line in f:
        obj = re.findall(regex,line)
        if(obj):
            obj = re.sub(regex,replacement,line)
            print(obj)
    f.close()
    choice = input("Choice (s/x): ")
    
print("Good bye")