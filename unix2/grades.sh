#!/bin/bash
#read a student name from STDIN
#capture the mark of the student from argument
#Determine and show the grade based on the mark

echo -n "Name: "
read name

mark=$1

if [ $mark -ge 85 ]
then
	grade="HD"
elif (($mark >= 75))
then
	grade="D"
elif [ $mark -ge 65 ]
then
	grade="C"
elif (($mark >= 50))
then
	grade="P"
else
	grade="Z"
fi
echo "$name mark is $mark and grade is $grade"
