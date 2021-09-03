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
	echo "nums=(${nums[*]})"
	local res=$(sum)
	echo "Array Sum = $res"
}

show
