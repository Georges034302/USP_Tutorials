#!/bin/env python3

data = input('String: ')

# Write operation
handler = open('data.txt','a')
handler.write(data+"\n")
handler.close()

# Read operation
handler = open('data.txt','r')
content = handler.read()
print(content)
handler.close()