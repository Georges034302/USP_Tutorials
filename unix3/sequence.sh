#!/bin/bash
#create a sequential array and show the sum and average of even numbers

nums=($(seq 2 3 50))

echo "Sequential array: ${nums[@]}"

for e in ${nums[@]}
do
	if [ $(($e%2)) == 0 ]
	then
		#let sum=$sum+$e
		sum=$(($sum+$e))
	fi
done

echo "Even sum = $sum"
length=${#nums[@]}
echo "Length = $length"
average=$(echo "scale=2;$sum/$length" |bc)
echo "Average = $average"
