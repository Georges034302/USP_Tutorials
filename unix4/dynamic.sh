#!/bin/bash
#Create a dynamic array of size n
#n is an argument to the script


n=$1
i=0
nums=()

while [ $i -lt $n ]
do
	echo -n "Number: "
	read num
	nums[$i]=$num
	((i++))
done

echo "Dynamic array: ${nums[@]}"
