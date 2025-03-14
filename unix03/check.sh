#!/bin/bash

#write a script to check if a string (from STDIN)
#is a dir, or a file.
#If the string does not exist, prompt the user to create
# a file or directory

read -p "String: " s

if [ -f $s ]
then
	echo "$s is a file"
elif [ -d $s ]
then
	echo "$s is a directory"
else
	echo -e "$s does not exist!\n"
	read -p "Create (f/d): " prompt
	if [ $prompt == "f" ]
	then
		touch $s
	else
		mkdir $s
	fi
fi
