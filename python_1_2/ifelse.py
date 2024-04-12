#!/bin/env python3

# Enter username and password
# check if the login is correct:
# correct username: admin
# correct password: superuser
username = input('Username: ')
password = input('Password: ')

if username == 'admin' and password == 'superuser':
    print('correct login') 
else: 
    print('Incorrect credentials')
    
