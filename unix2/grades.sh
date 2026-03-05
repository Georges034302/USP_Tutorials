#!/bin/bash

# Read student name from STDIN
# Capture student mark from arg
# Determine the grade

read -p "Student name: " name

if [ $1 -ge 85 ]
then
	grade="HD"
elif [ $1 -ge 75 ]
then
	grade="D"
elif [ $1 -ge 65 ]
then
	grade="C"
elif [ $1 -ge 50 ]
then
	grade="P"
else
	grade="Z"
fi
echo "$name's mark is $1 and grade is $grade"
