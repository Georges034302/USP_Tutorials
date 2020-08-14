#!/bin/bash
#print a list of integers from 1 to 10 and their power

for ((i=1;i<=10;i++))
do
	pow=$((($i*$i)+($i+2)))
	echo "$i --> $pow" 
done
