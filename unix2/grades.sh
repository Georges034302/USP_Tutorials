#!/bin/bash
#Determine the grades of the current user based
#on their marks passed on as argument

echo "Student $(whoami) record..."

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



echo "Your mark  is: $1"
echo "Your grade is: $grade"
