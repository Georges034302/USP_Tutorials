#!/bin/bash

# Read an integer n from STDIN
# Show all values between 0 and n
#NOTE: use a while-loop

echo -n "n = "
read n

i=0
while [ $i -le $n ]
do
	echo $i
	((i++))
done
