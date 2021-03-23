#!/bin/bash
#Write a script that generates a sequential array
#function that calculates the sum of array elements
#function that prints the array and the sum

nums=($(seq 2 3 30))

function sum(){
	for e in ${nums[@]}
	do
		sum=$(($sum+$e))
	done
	echo $sum
}

function show(){
	echo "nums=(${nums[*]})"
	local res=$(sum)
	echo "Array sum = $res"
}

show

