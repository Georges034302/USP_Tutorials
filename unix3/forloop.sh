#!/bin/bash

# Read integer from STDIN
# Show all numbers from 0 to the value entered

read -p "n = " n

for((i=0;i<=$n;i++))
do
	echo "$i"
done

# Now only show the even numbers
echo
for e in $(seq 0 $n)
do
	if [ $(($e%2)) == 0 ]
	then
		echo $e
	fi
done

