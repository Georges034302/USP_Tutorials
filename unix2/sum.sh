#!/bin/bash
#calculate the sum of integers from user input until -1
#Determine the maximum integer 

#read pattern
echo -n "Number: "
read num
max=0

while [ $num -ne -1 ]
do
	sum=$(($sum+$num))
	if [ $num -gt $max ]
	then
		max=$num
	fi
	echo -n "Number: "
	read num
done
echo "Sum = $sum"
echo "Max = $max"
