#!/bin/bash

# A function is a method that returns a value
# A function is always a noun
# A function can be stored into a variable

# Write a function that calculate the factorial of n
# n is an integer argument for the function
# Write a procedure to read a value from STDIN
# then show the factorial of that value

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






