#!/bin/bash

#Req:
# Read a positive integer n from STDIN
# Show every value from 0 to n and their power

read -p "n = " n

for((i=0;i<=$n;i++))
do
	p=$(($i*$i))
	echo "$i --> $p"
done
