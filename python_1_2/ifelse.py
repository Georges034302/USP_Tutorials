#!/bin/env python3

# Check if the username and password are correct
# HINT: username--> superuser and password: super123
username = input('Username: ')
password = input('Password: ')

if username == 'superuser' and password == 'super123':
    print(f'Welcome {username}')
else:
    print(f'Incorrect credentials!')

print('Thank You')

