#!/bin/bash

# Write a function to calculate the factorial of n
# n is captured from argument
# define a procedure to read a value from STDIN
# then calculate the factorial of that value

function factorial(){
	local n="$1"
	local f=1
	for((i=2;i<=$n;i++))
	do
		f=$(($f*$i))
	done
	return $f
}

function calculate(){
	read -p "n = " n
	factorial $n
	local result=$?
	echo "Factorial($n) = $result"
}
calculate

