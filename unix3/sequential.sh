#!/bin/bash

#generate a sequential array
#calculate the sum of even elements
#show the total

start=5
step=3
end=30

numbers=($(seq $start $step $end))

echo "Sequential array --> ${numbers[@]}"

length=${#numbers[@]}

for((i=0;i<$length;i++))
do
	if [ $((${numbers[$i]}%2)) == 0 ]
	then
		sum=$(($sum+${numbers[$i]}))
	fi
done

echo "Even sum = $sum"
