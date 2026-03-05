#!/bin/bash

# Check if an argument is a dir or a file
# if the argument does not exist then allow the user to:
# - (d) create a directory
# - (f) create a file

if [ -d $1 ]
then
	echo "$1 is a directory"
elif [ -f $1 ]
then
	echo "$1 is a file"
else
	echo -n "Create (d/f): "
	read choice
	if [ "$choice" = "d" ]
	then
		mkdir $1
	else
		touch $1
	fi
fi
