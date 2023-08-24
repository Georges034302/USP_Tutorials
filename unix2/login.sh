#!/bin/bash
# Requirements:
# Read in username and password
# validate username and password with
# jim1234 and super

read -p "Username: " username
read -p "Password: " -s password

if [[ $username == "jim1234" && $password == "super" ]]
then
	echo -e "\nWelcome Jim"
else
	echo -e "\nIncorrect credentials"
fi
