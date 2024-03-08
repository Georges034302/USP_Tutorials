#!/bin/bash

# Read name from STDIN
# Welcome the name if george
# then thank you

read -p "Name: " name

if [ $name == "george" ]
then
	echo "Welcome $name"
fi

echo "Thank You!"


