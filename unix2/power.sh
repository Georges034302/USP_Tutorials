#!/bin/bash
#read a value n from STDIN
#display the power(2) series of n

echo -n "N = "
read n

for ((i=0;i<=$n;i++))
do
	pow=$(($i*$i))
	echo "$i --> $pow"
done
