#!/bin/bash
#create a sequential array from start to end using a jump
#print the array all in one line
#calculate the average

start=$1
jump=$2
end=$3

nums=($(seq $start $jump $end))

echo "Sequential array: ${nums[@]}"

for e in ${nums[@]}
do
	sum=$(($sum+$e))
done

echo "Sum = $sum"
length=${#nums[@]}
echo "Length = $length"
average=$(echo "scale=2;$sum/$length" | bc)

echo "Average = $average"
