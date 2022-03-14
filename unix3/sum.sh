#!/bin/bash
#Add all numbers entered from STDIN until -1

echo -n "N = "
read n

sum=0

while [ $n -ne -1 ]
do
	sum=$(($sum+$n))
	echo -n "N = "
	read n
done

echo "Sum = $sum"
