#!/bin/bash

# A function:
# - noun
# - returns a value
# - the returned value can be saved into a variable

# Read n from STDIN until -1
# Define a function to calculate the factorial of n
# Show the factorial of n

function factorial(){
	local n="$1"
	local f=1
	for((i=2;i<=$n;i++))
	do
		f=$(($f*$i))
	done
	return $f
}

read -p "n = " n

while [ $n -ne -1 ]
do
	factorial $n
	let result=$?
	echo "Factorial($n) = $result"
	read -p "n = " n
done
