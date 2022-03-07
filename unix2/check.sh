#!/bin/bash
#Check if a name given from STDIN is a file or directory
#If the name does not exist prompt the user to create it
#as a a directory or a file

echo -n "Enter a name: "
read name

if [ -d $name ]
then
	echo "$name is a directory"

elif [ -f $name ]
then
	echo "$name is a file"

else #name does not exist
	echo -n "$name does not exist, what is your choice?(d/f): "
	read choice

	if [ $choice == "d" ]
	then
		mkdir $name
	else
		touch $name
	fi
fi
ls -l
