#!/bin/bash

#Enter student name from STDIN
#Get the student mark from argument
#Show the name and the grade of the student

echo -n "Name: "
read name

if [ $1 -ge 85 ]
then
	grade="HD"
elif (($1 >= 75))
then
	grade="D"
elif [ $1 -ge 65 ]
then
	grade="C"
elif [ $1 -ge 50 ]
then
	grade="C"
else
	grade="Z"
fi

echo "$name grade is $grade"
