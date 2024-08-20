#!/bin/bash

# Print all values and their squares between first and last
# First and last are arguments
# Step by 3

first=$1
last=$2
step=$3

for e in $(seq $first $step $last)
do
	echo "$e --> $(($e*$e))"
done
