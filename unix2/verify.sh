#!/bin/bash
#Verify if the name entered from STDIN is the username

echo -n "Name: "
read name


if [ $name == $(whoami) ]
then
	echo "Welcome $name"
else
	echo "Goodbye!!!"
fi
