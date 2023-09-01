#!/bin/bash

#Requirements:
# Check if an argument is a directory or a file
# Otherwise ask the user to create directory or file

if [ -d $1 ]
then
	echo "$1 is s directory"
elif [ -f $1 ]
then
	echo "$1 is a file"
else
	echo "$1 does not exist"
	read -p "Create(d/f): " choice
	if [ "$choice" == "d" ]
	then
		mkdir $1
	elif [ "$choice" == "f" ]
	then
		touch $1
	else
		echo "Unknown command"
	fi
fi

