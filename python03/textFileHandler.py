#!/bin/env python3

# Read a string from STDIN
# Write the string to a text file  
# Read from the text file
# Print the content of the file  

string = input('String: ')

# Writing data to a file
f = open('demo.txt','a')
f.write('string+'\n'')
f.close()

# Reading data from a file  
f = open('demo.txt','r')
print(f.read())
f.close()
