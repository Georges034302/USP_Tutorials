#!/bin/bash

# nested-if
#
# if [ <boolean 1 > ]
# then
#	<code 1>
#	if [ <boolean 2> ]
#	then
#		<code 2>
#	else
#		<code 3
#	fi
# else
#	<code 4
# fi
#Req: Read an integer n from STDIN
#	check if n is positive
#		if so, check if n is even or odd
#	otheriwse n is negative

#read-pattern
# echo -n "n = "
# read n

read -p "n = " n

if [ $n -ge 0 ]
then
	if [ $(($n%2)) == 0 ]
	then
		echo "$n is even"
	else
		echo "$n is odd"
	fi
else
	echo "$n is negative"
fi
















