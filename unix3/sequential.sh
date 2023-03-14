#!/bin/bash

#Create the sequential array using arguments
#Calculate and show the even-sum

#sequential array starting wwith 1, jumping by 3, ending at 50
numbers=($(seq $1 $2 $3))

echo "Sequential array: ${numbers[@]}" #print the whole array

length=${#numbers[@]}

sum=0

for n in ${numbers[@]}
do
	if [ $(($n%2)) == 0 ]
	then
		sum=$(($sum+$n))
	fi
done
echo "Even Sum = $sum"
