#!/bin/bash

# Enter integer n from STDIN
# Show every value from 0 to n and its square

read -p "n = " n

for((i=0;i<=$n;i++))
do
	echo "$i --> $(($i*$i))"
done
