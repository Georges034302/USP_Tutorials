#!/bin/bash

# Read integers from STDIN until -1 is entered
# Show the total value

read -p "n = " n

sum=0

while [ $n -ne -1 ]
do
	sum=$(($sum+$n))
	read -p "n = " n
done

echo "Total = $sum"

