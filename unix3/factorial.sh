#!/bin/bash

# Read n from STDIN until -1
# Show the factorial of n

read -p "n = " n

while [ $n -ne -1 ]
do
	f=1
	for((i=2;i<=$n;i++))
	do
		f=$(($f*$i))
	done
	echo "Factorial($n) = $f"
	read -p "n = " n
done
