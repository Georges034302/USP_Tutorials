#!/bin/bash

# Enter integer from STDIN
# check if the value is even or odd or negative

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
