#!/bin/bash
#read integers until -1
#calculate and show the total of values
#determine and show the max value entered

echo -n "N = "
read n

sum=0
max=0

while [ $n -ne -1 ]
do
	sum=$(($sum+$n))

	if [ $max -le $n ]
	then
		max=$n
	fi

	echo -n "N = "
	read n
done

echo "SUM = $sum"
echo "MAX = $max"
