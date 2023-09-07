#!/bin/bash

#Req:
# Define a function 'factorial' to calculate the 
# factorial of n (positive intefer)
# Define a procedure 'calculate' to read n from STDIN
# show the factorial of n

function factorial(){
	local n=$1
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
	local f=$?
	echo "Factorial($n) = $f"
}

calculate


