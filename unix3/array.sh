#!/bin/bash
#Create an array of elements
#print the array
#Print the length of the array
#Show the array elements one on each line

nums=(Hello Welcome USP 32547 George 034302)

echo "My first array: ${nums[@]}"
length=${#nums[@]}
echo "Array length = $length"

for((i=0;i<$length;i++))
do
	echo ${nums[$i]}
done


