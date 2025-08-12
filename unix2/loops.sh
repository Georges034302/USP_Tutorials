#!/bin/bash

# read integer n from STDIN
# show all values and its squares from 0 to n

read -p "n = " n

echo "Using a for-loop ..."
for((i=0;$i <= $n;i++))
do
	echo "$i - $(($i*$i))"
done

echo
echo "Using a while-loop ..."

i=0

while [ $i -le $n ]
do
	echo "$i - $(($i*$i))"
	((++i))
done
