#!/bin/bash
#Determine the sum of integers from user input until -1
#Determine the max value of entries

#read pattern
echo -n "Number: "
read num
sum=0
max=0

#while-loop pattern
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

#output pattern
echo "Sum = $sum"
echo "Max = $max"
