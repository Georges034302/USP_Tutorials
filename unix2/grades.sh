#!/bin/bash
#Print a student name
#Determine the student grade based on their argument mark

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
echo "Student grade is: $grade"
