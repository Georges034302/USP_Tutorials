#!/bin/bash
#check if a number from STDIN is greater than 10
#otherwise it is less than 10

read -p "n = " n

if [ $n -gt 10 ]
then
	echo "$n > 10"
else
	echo "$n <= 10"
fi

echo "Thank you"

