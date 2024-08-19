#!/bin/bash

# Read n from STDIN
# Only show the even n numbers
# Stop when -1 is entered

read -p "n = " n

while [ $n -ne -1 ]
do
	if [ $(($n%2)) -eq 0 ]
	then
		echo "$n"
	fi
	read -p "n = " n
done
