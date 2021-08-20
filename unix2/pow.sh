#!/bin/bash

#Display 10 digits and its power of 2 side by side

for ((i=1;i<=10;i++))
do
	pow=$(($i*$i))
	echo "$i ---> $pow"
done
