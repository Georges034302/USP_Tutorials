#!/bin/bash
#create an array dynamically from STDIN
#size of the array is set from argument
#print the array

n=$1

nums=() #empty array

i=0

while [ $i -lt $n ]
do
	echo -n "Value = "
	read val

	nums[$i]=$val

	((i++))
done

echo "Dynamic array: ${nums[@]}"
