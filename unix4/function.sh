#!/bin/bash
nums=($(seq 2 3 20))

function sum(){
	for e in ${nums[@]}
	do
		sum=$(($sum+$e))
	done
	echo $sum
}

function show(){
	local result=$(sum)
	echo "Sum = $result"
}

show
