#!/bin/bash

#Req:
# show all the values and their squares from 1 to n
# n is the first positive integer argument
# NOTE: you must use functions

function square(){
	local n=$1
	for((i=1;i<=$n;i++))
	do
		echo "$i --> $(($i*$i))"
	done
	echo
}

square $1
square $2
square $3
