#!/bin/bash

# Read n integer from STDIN until -1 is entered
# Add all the even numbers then show the total

read -p "n = " n

while [ $n -ne -1 ]
do
	if [ $(($n%2)) -eq 0 ]
	then
		sum=$(($sum+$n))
	fi
	read -p "n = " n
done
echo "TOTAL = $sum"

