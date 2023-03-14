#!/bin/bash

items=(2 hi 3.5 bye 44) #creating an array

length=${#items[@]} 	#how many items in the array
			# @represents indexs from 0 to 4
echo "Array length = $length"

for((i=0;i<$length;i++))
do
	echo "Items[$i] = ${items[$i]}"
done

j=0

while [[ $j -lt $length ]]
do
	echo "${items[$j]}"
	((j++))
done

for e in ${items[@]}
do
	echo "$e"
done
