#!/bin/bash

#Enter a name from STDIN
#check if the name is George
#if the name is George, output welcome and the name
#otherwise output goodbye

echo -n "Name: "
read name

if [ $name == "George" ]
then
	echo "welcome $name"
else
	echo "goodbye"
fi
