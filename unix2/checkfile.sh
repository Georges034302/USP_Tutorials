#!/bin/bash

# Read a name from STDIN
# Check if the name: exists, directory, file
# Check the name permissions if it exists
# If the name does not exist, offer the user to create file or dir
#NOTE: use -e (exist), -d (dir), -f (file), -r (read), -w (write), -x (exe)

read -p "Name: " name

if [ -e $name ]; then
	if [ -d $name ]; then
		echo "$name is a directory"
	else # check all permissions for a file
		echo "$name is a file"
		if [ -r $name ]; then
			echo " - $name is readable"
		fi
		if [ -w $name ]; then
			echo " - $name is writable"
		fi
		if [ -x $name ]; then
			echo " - $name is executable"
		fi

	fi
else
	echo "$name does not exist!"
	echo
	echo -n "Create (f/d): "
	read op

	if [ $op == "d" ]; then
		mkdir $name
	else
		touch $name
	fi
fi
