#!/bin/bash
# Read an integer n from STDIN
# show all values from 0 to n

read -p "n = " n

for((i=0;i<=$n;i++))
do
	echo $i
done

echo
# Now show only the even numbers
#NOTE: use for-each loop
for e in $(seq 0 $n)
do
	if [ $(($e%2)) == 0 ]
	then
		echo $e
	fi
done

