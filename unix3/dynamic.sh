#!/bin/bash
#create a dynamic array of size n from argument

n=$1 #Size of the array
nums=() #empty array to populate later

i=0

while [[ $i -lt $n ]]
do
	echo -n "Value = "
	read value
	nums[$i]=$value #save the value from STDIN in the array
	((i++))
done

echo "Array: ${nums[@]}"
