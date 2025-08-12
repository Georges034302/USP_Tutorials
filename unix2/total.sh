#!/bin/bash

# Read positive integers from STDIN until zero
# Add all values

read -p "n = " n

sum=0

while [ $n -ne 0 ]
do
	sum=$(($sum+$n))
	read -p "n = " n
done
echo "TOTAL = $sum"
