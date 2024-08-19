#!/bin/bash

# Read an integer n from STDIN and check if n is odd, even, or negative

read -p "n = " n

if [ $n -ge 0 ]
then
	if [ $(($n%2)) -eq 0 ]
	then
		echo "$n is even"
	else
		echo "$n is odd"
	fi
else
	echo "$n is negative"
fi
