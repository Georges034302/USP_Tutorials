#!/bin/bash


# Read integer n from STDIN until -1
# Add all the even values
# Show the total

read -p "n = " n
sum=0

while [ $n -ne -1 ]
do
	if [ $(($n%2)) == 0 ]
	then
		sum=$(($sum+$n))
	fi
	read -p "n = " n
done
echo "Even-Sum = $sum"
