#!/bin/bash
#create and array from arguments
#Print the array using a for-each

array=($*) #array from first 4 arguments

length=${#array[@]} #length of the array

for e in ${array[@]}
do
	echo $e
done
