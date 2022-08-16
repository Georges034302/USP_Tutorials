#!/bin/bash

#Read n-values from STDIN while n is not -1
#Add all the even-values and show the total
#Show the maximum entered value

echo -n "N = "
read n

sum=0
max=0
while [ $n -ne -1 ]
do
	if (($n % 2 == 0))
	then
		sum=$(($sum+$n))
	fi

	if [ $n -gt $max ]
	then
		max=$n
	fi

	echo -n "N = "
	read n
done

echo
echo "Total = $sum"
echo "Max = $max"
