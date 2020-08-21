#!/bin/bash
#Create a dynamic array of size n from argument
#Show the array

n=$1
i=0
nums=()

while [ $i -lt $n ]
do
	echo -n "Value = "
	read val
	nums[$i]=$val
	((i++))
done

echo "Dynamic array: ${nums[@]}"
