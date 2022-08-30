#!/bin/bash

#Read an integer between 0 and 255
#Convert this integer to binary
#Show the binary representation

#read a number between 1 and 255
echo -n "Number = "
read n

#create an array of 8 zeroes
zeroes=(0 0 0 0 0 0 0 0)

array=()

length=${#zeroes[@]}

for((i=0;i<$length;i++))
do
	array[$i]=$(($n%2))
	n=$(($n/2))
done

#echo ${array[@]}

binary=()

j=0

for((i=$length-1;i>=0;i--))
do
	binary[$j]=${array[$i]}
	((j++))
done

echo "Binary: ${binary[@]}"
