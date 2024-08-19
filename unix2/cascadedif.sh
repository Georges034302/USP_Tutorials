#!/bin/bash

#Read student name from STDIN
#Get student mark from argument
#Determine the grade based on the mark

read -p "Student name: " name

mark=$1

if [ $mark -ge 85 ]
then
	grade="HD"
elif [ $mark -ge 75 ]
then
	grade="D"
elif [ $mark -ge 65 ]
then
	grade="C"
elif [ $mark -ge 50 ]
then
	grade="P"
else
	grade="Z"
fi
echo "$name mark is $mark and grade is $grade"
