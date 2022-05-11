#!/bin/env python3
import mymodule as m
import pprint

def main():
    first = int(m.read("First = "))
    last = int(m.read("Last = "))
    size = int(m.read("Size = "))
    mylist = m.ranlist(first,last,size)
    print("Random list: {}".format(mylist))
    names = m.dynamicdictionary(mylist)
    pp = pprint.PrettyPrinter(indent=2,width=40)
    print("------------------Sorted dictionary ----------------")
    pp.pprint(names)
    m.sort(names)
    print("-----------------------------------------------------")
    key = int(m.read("Update by key: "))
    name = m.read("New name: ")
    m.update(names,key,name)
    print("------------------dictionary after update----------------")
    m.sort(names)

    key = int(m.read("Delete by key: "))
    m.delete(names,key)    
    print("------------------dictionary after delete----------------")
    m.sort(names)

main()
