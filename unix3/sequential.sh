#!/bin/bash
#Generate a sequential array
#Show the array and length
#Show the even-sum and average
start=$1
jump=$2
end=$3
nums=($(seq $start $jump $end))
length=${#nums[@]}

echo "Sequential array: ${nums[@]}"
echo "Length = $length"

for e in ${nums[@]}
do
	if [ $(($e%2)) == 0 ]
	then
		#let sum=$sum+$e
		sum=$(($sum+$e))
	fi
done

echo "Sum = $sum"
average=$(echo "scale=5;$sum/$length" | bc)
echo "Average = $average"


