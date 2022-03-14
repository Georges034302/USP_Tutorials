#!/bin/bash
#Calculate the factorial of n
#n is an argument to the script

n=$1

f=1
for((i=1;i<=$n;i++))
do
	f=$(($f*$i))
done

echo "Factorial($n) = $f"
