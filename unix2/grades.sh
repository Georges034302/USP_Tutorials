#!/bin/bash
#Print the username
#Determine the user grade based on the mark argument

echo "> Student $(whoami) file: "

if [ $1 -ge 85 ]
then
	grade="HD"
elif (($1 >= 75))
then
	grade="D"
elif [ $1 -ge 65 ]
then
	grade="C"
elif (($1 >= 50))
then
	grade="P"
else
	grade="Z"
fi

echo "$1 grade is $grade"
