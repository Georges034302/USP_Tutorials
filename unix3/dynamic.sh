#!/bin/bash

#read integer values from STDIN until -1 is entered
#store the values in an array
#show the array

numbers=() #empty array

echo -n "N = "
read n

i=0  #elements index

while [ $n -ne -1 ]
do
	numbers[$i]=$n

	echo -n "N = "
	read n

	((i++))
done

echo "Dynamic array --> ${numbers[@]}"

