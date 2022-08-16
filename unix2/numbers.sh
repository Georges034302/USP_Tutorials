#!/bin/bash

#show the numbers starting from first until last values from STDIN
#show the square of every number

echo -n "First = "
read first
echo -n "Last = "
read last

for((i=$first;i<=$last;i++))
do
	echo "$i --> $(($i*$i))"
done
