#!/bin/bash

#create an array
#show the length of the array
#show the elements of the array each on a line
#show the array object

numbers=(USP 32547 Spring 2022)

length=${#numbers[@]}

echo $length

for((i=0;i<$length;i++))
do
	echo "element[$i] = ${numbers[$i]}"
done

echo "Array --> ${numbers[@]}"


