#!/bin/bash

# Read student name from STDIN
# Get student mark from arguments
# Show the student grade based on the mark

read -p "student: " name
mark=$1

if [ $mark -ge 85 ]
then
	grade="HD"
elif [ $mark -ge 75 ]
then
	grade="D"
elif (($mark>=65))
then
	grade="C"
elif [ $mark -ge 50 ]
then
	grade="P"
else
	grade="Z"
fi
echo "Student $name mark=$mark and grade is $grade"
