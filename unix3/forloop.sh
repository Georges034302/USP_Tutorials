#!/bin/bash

#Req:
# Read positive integer n from STDIN
# Show every value from 0 to n and its power

echo -n "n = "
read n

for((i=0;i<=$n;i++))
do
	pow=$(($i*$i))
	echo "$i --> $pow"
done
