#!/bin/bash

# cascaded if-statement syntax:

# if [ <boolean expr> ]
# then
# 	<code 1>
# elif [ <boolean expr> ]
# then
#	<code 2>
# elif [ <boolean expr> ]
# then
#	<code 3>
#  
# ...............
# else
# 	<code n>
# fi
# Req: 	Read student name from STDIN
#	Consume student integer mark from arg
#	Determine and show the grade based
#	on the mark
echo -n "Student name: "
read name

if [ $1 -ge 85 ]
then
	grade="HD"
elif (($1 >= 75))
then
	grade="D"
elif [ $1 -ge 65 ]
then
	grade="P"
elif (($1 >= 50))
then
	grade="C"
else
	grade="Z"
fi
echo "$name mark is $1 and grade is $grade"

















