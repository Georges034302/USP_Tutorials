#!/bin/bash
#Write a bash script that determines the grades of students based on their marks

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

echo "You grade is $grade"
echo
