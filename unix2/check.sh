#!/bin/bash

#Enter a name from STDIN
#check if the name is a file, or a directory or if it doesn't exist

echo -n "Name: "
read name

if [ -d $name ]
then
	echo "$name is a directory"
elif [ -f $name ]
then
	echo "$name is a file"
else
	echo "$name does not exist in the folder!"
	echo "Would you like to make $name a file or directory (f/d): "
	echo
	echo -n "Create (f/d): "
	read choice

	if [ $choice == "f" ]
	then
		touch $name
		ls -l $name
	elif [ $choice == "d" ]
	then
		mkdir $name
		ls -l $name
	else
		echo "Unknown command $choice !"
	fi
fi
