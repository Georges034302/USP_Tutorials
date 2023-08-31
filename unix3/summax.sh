#!/bin/bash
#Req:
# Read n integer from STDIN until -1
# Determine the maximum value entered
# Calculate the total of entered values
# Show sum and max

read -p "n = " n

sum=0
max=0

while [ $n -ne -1 ]
do
	sum=$(($sum+$n))
	if [ $n -gt $max ]
	then
		max=$n
	fi
	read -p "n = " n
done

echo "Sum = $sum"
echo "Max = $max"
