#!/bin/bash

# Read n integer from STDIN
# Show all the values from 0 to n
# Show the factorial of n

read -p "n = " n

for((i=0;i<=$n;i++))
do
	echo "$i"
done

f=1
for((i=2;i<=n;i++))
do
	f=$(($f*$i))
done
echo "Factorial($n) = $f"
