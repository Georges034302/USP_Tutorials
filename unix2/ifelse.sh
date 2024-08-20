#!/bin/bash

# Read username and password from STDIN
# Verify that username is admin and password is super123

echo -n "Username: "
read username

read -p "Password: " password

if [[ $username == "admin" && $password == "super123" ]]
then
	echo "Welcome"
else
	echo "Incorrect credentials"
fi
