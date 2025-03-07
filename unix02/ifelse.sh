#!/bin/bash

# Read username and password from STDIN
# check if the username is george
# check if the password is super123

read -p "username: " username
read -p "password: " password

if [[ $username == "george" && $password == "super123" ]]
then
	echo "Welcome $username"
else
	echo "Goodbye!"
fi

