#!/bin/bash
#create and show a sample array and also print every element on a new line

array=(1 2 3 hello welcome to USP)
echo ${array[@]}
length=${#array[@]}
echo "Length = $length"

for((i=0;i<$length;i++))
do
	echo "element[$i] = ${array[$i]}"
done
