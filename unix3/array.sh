#!/bin/bash
#create an array and show the following:
#1- Length of the array
#2- Each element of the array on a new line

array=(1 2 3 welcome to USP 32547)

length=${#array[@]}

echo "Length of the array is: $length"

for((i=0;i<$length;i++))
do
    echo "element[$i] = ${array[$i]}"
done

