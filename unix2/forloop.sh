#!/bin/bash

# Read an integer n from STDIN
# show all values from zero to n
# show the power of each value

read -p "n = " n

for((i=0;i<=$n;i++))
do
	echo "$i --> $(($i*$i))"
done
