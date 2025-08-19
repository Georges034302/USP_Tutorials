#!/bin/bash

# Read integers from STDIN until -1
# Add all even numbers

sum=0

read -p "n = " n

while [ $n -ne -1 ]
do
	if [ $(($n%2)) -eq 0 ]; then
		sum=$(($sum+$n))
	fi
	read -p "n = " n
done
echo "Even Sum = $sum"
