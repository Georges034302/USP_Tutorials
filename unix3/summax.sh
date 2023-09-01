#!/bin/bash

#Req:
# Read integer value n from STDIN until -1
# Calculate the sum of all values and max value
# Show the sum and max

sum=0
max=0

read -p "n = " n

while [ $n -ne -1 ]
do
	sum=$(($sum+$n))
	if [ $n -gt $max ]
	then
		max=$n
	fi
	read -p "n = " n
done

echo "MAX = $max"
echo "SUM = $sum"
