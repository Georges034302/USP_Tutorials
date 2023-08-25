#!/bin/bash

# Requirements
# Read username and password
# Verify that username is "jim123"
# Verify that password is "super"
# Ensure that password typing is hidden

read -p "Username: " user
read -p "Password: " -s pass

if [[ $user == "jim123" && $pass == "super" ]]
then
	echo -e "\nWelcome Jim"
else
	echo -e "\nIncorrect credentials"
fi

