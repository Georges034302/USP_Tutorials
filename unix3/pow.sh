#!/bin/bash
#print n numbers and their power
#n is captured from STDIN

echo -n "N = "
read n

echo "For loop"
for((i=1;i<=$n;i++))
do
	p=$(($i*$i))
	echo "$i ---> $p"
done
echo

echo "While loop"
i=1
while [ $i -le $n ]
do
	p=$(($i*$i))
	echo "$i ---> $p"
	((i++))
done
