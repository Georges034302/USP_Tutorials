#!/bin/bash
#Requirements:
# Check if an argument is a file or directory
# Otherwise, prompt the user to create a file or directory

if [ -d $1 ]
then
	echo "$1 is a directory"
elif [ -f $1 ]
then
	echo "$1 is a file"
else
	echo "$1 does not exist"
	read -p "Create(d/f): " choice

	if [ "$choice" == "d" ]
	then
		mkdir $1
	else
		touch $1
	fi
fi

echo "Thank you"
