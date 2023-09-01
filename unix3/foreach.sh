#!/bin/bash

#Req 1:
# Show a sequence of values between first and last
# first and last are from arguments (first < last)

for e in $(seq $1 $2)
do
	echo $e
done

#Req 2:
# Show a sequence of values from first to last
# jump by a value from STDIN (first < jump < last)
echo

read -p "jump = " jump

for e in $(seq $1 $jump $2)
do
	echo $e
done
