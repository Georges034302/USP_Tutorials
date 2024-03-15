#!/bin/bash

# Read integer n from STDIN until -1
# Determine the min and max
# Show the  min and max

read -p "n = " n
max=0
min=1000000000000000
while [ $n -ne -1 ]
do
	if [ $n -gt $max ]
	then
		max=$n
	fi
	if [ $n -lt $min ]
	then
		min=$n
	fi
	read -p "n = " n
done
echo "MIN = $min"
echo "MAX = $max"
