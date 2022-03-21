#!/bin/bash
#Generate a sequential array starting with 2 ending with 30
#Moving by a step of 3
#Show the sum of the elements in this array
start=2
jump=3
end=30
nums=($(seq $start $jump $end))

length=${#nums[@]}

echo "Sequential array: ${nums[@]}"

sum=0
i=0

while [ $i -lt $length ]
do
	sum=$(($sum+${nums[$i]}))
	((i++))
done
echo "Sum = $sum"
