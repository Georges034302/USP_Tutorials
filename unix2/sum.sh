#!/bin/bash

#Read numbers from STDIN until -1
#Add all numbers
#Display the total
#Dispplay the maximum number


#Read number from STDIN - READ Pattern
echo -n "Number: " #The prompt
read num

sum=0
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
