#!/bin/bash
#Create a sample array and show the length and the entire array
#Then show each element of this array

array=(1 2 3 hello welcome to USP)

echo ${array[@]}

length=${#array[@]}
echo "Length = $length"

for((i=0;i<$length;i++))
do
	echo "element[$i]= ${array[$i]} "
done
