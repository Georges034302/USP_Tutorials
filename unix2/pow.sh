#!/bin/bash
#Print a list of 10 integers and their power

for ((i=1;i<=10;i++))
do
	pow=$((($i*$i)+($i+2)))
	echo "$i --> $pow"
done
