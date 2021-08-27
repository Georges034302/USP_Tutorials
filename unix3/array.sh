#!/bin/bash
#Create an array
#store the length of the array into a variable
#Print all the elements of the array

array=(welcome to USP 32547 Spring 2021) #creating an array

length=${#array[@]} #Length of the array

echo "Length of the array: $length"

for((i=0;i<$length;i++))
do
	echo "array[$i] = ${array[$i]}"
done
