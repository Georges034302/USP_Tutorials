#!/bin/bash

# Read a name from STDIN and check if the name is Tom

echo -n "Name: "
read name

if [ $name == "Tom" ]
then
	echo "welcome $name"
fi
