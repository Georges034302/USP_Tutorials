#!/bin/bash

# cascaded-if
#
# if [ <boolean 1> ]
# then
#	<code 1>
# elif [ <boolean 2> ]
#	<code 2>
# elif [ <boolean 3> ]
#	<code 3>
# ..................
# ..................
# else
#	<code n>
# fi

#Req:
# Read student name from STDIN
# Consume sudent mark from arguments
# Determine the grade based on the mark
# Show the results

read -p "Student name: " name

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
echo "$name mark is $1 and grade is $grade"
















