#!/bin/bash

# Read integer from STDIN, and check:
# is the integer even
# is the integer odd
# is the integer negative

echo -n "n = "
read n

if [ $n -gt 0 ]
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



