#!/bin/bash

numbers=(3 4 1 4 9)

function sum(){
	total=0
	for e in ${numbers[@]}
	do
		total=$(($total+$e))
	done
	echo $total
}

function run(){
	echo "${numbers[@]}"
	local result=$(sum) #calling the function sum
	echo "Total = $result"
}

run
