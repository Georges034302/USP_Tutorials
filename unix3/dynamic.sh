#!/bin/bash
#Create a dynamic array from user input with a size n from argument

n=$1
nums=()

i=0

while [ $i -lt $n ]
do
	echo -n "Value: "
	read val
	nums[$i]=$val
	((i++))
done

echo "Dynamic array: ${nums[@]}"
