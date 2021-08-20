#!/bin/bash

#Display the name of the user
#For a given mark argument display the relative grade

echo "Student $(whoami) grades."

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

echo "$(whoami) grade is $grade"
