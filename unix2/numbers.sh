#!/bin/bash

# Read an integer from STDIN
# Check if the integer is zero, even, odd, negative

read -p "n = " n

if [ $n -eq 0 ]; then
	echo "$n is zero"
elif [ $n -lt 0 ]; then
	echo "$n is negative"
else
	if [ $(($n%2)) -eq 0 ]; then
		echo "$n is even"
	else
		echo "$n is odd"
	fi
fi
