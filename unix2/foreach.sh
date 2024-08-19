#!/bin/bash

first=$1
last=$2
step=$3

for e in $(seq $first $step $last)
do
	echo "$e --> $(($e*$e))"
done


