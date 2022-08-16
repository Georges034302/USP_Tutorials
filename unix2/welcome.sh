#!/bin/bash

#Write a script that checks if the user from STDIN is George

echo -n "Enter your name: "
read name

if [ $name == "George" ]
then
	echo "Welcome $name"
else
	echo "Goodbye!!!"
fi
