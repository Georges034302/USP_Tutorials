#!/bin/bash

# Read  a string from STDIN
# Check if the string is a file, or a directory
# if the string does not exist, offer the user
# options to create a file or a directory

read -p "String: " string

if [ -f $string ]
then
	echo "$string is a file"
elif [ -d $string ]
then
	echo "$string is a directory"
else
	echo "$string does not exist"
	echo -n "Create (f/d): "
	read choice
	if [ "$choice" == "f" ]
	then
		touch $string
	else
		mkdir $string
	fi
fi
echo "verifying ..."
ls -l





