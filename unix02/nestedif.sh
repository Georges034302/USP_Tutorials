#!/bin/bash

# Read integer from STDIN
# check if the integer is even, odd, zero, or negative

read -p "n = " n

if [ $n -gt 0 ]
then
	echo "$n is positive"
	if [ $(($n%2)) -eq 0 ]
	then
		echo "$n is even"
	else
		echo "$n is odd"
	fi
elif [ $n -eq 0 ]
then
	echo "$n is zero"
else
	echo "$n is negative"
fi
