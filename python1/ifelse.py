#!/bin/python3
# Read username and password from STDIN
# Verify the values with:
# user --> superuser
# password --> hello1234

username = input('Username: ')
password = input('Password: ')

if (username == 'superuser' and password == 'hello1234'):
    print(f'Welcome {username}')
else:
    print('Incorrect credentials')

