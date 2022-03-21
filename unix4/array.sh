#!/bin/bash

numbers=(1 2 3 4 5 6 7 8 9 10)

length=${#numbers[@]}
echo "Length = $length"
echo ${numbers[@]}

for((i=0;i<$length;i++))
do
	if [ $(($i%2)) == 0 ]
	then
		echo -n $i " "
	fi
done
echo

total=0
for e in ${numbers[@]}
do
	total=$(($total+$e))
done
echo "Total = $total"
