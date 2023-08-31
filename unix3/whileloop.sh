#!/bin/bash

#Req:
# Read integer positive n from STDIN
# Show all values from 1 to n using while loop

read -p "n = " n

i=1

while [ $i -le $n ]
do
	echo $i
	((i++))
done
