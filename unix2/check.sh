#!/bin/bash
#read a file/dir name from STDIN
#validate that the name is a file or directory

echo -n "Name: "
read name

if [ -d $name ]
then
	echo "$name is a directory"
elif [ -f $name ]
then
	echo "$name is a file"
else
	echo "$name does not exist!"
	echo -n "make $name f/d: "
	read choice
	if [ $choice == "d" ]
	then
		mkdir $name
	elif [ $choice == "f" ]
	then
		touch $name
	else
		echo "unknown command"
	fi
fi

