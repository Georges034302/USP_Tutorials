#!/bin/bash

#Req:
# Read positive integer n from STDIN
# Show all values from 1 to n using a while loop;

i=1

read -p "n = " n

while [ $i -le $n ]
do
	echo $i
	((i++))
done



