#!/bin/bash

# Read n from STDIN until -1
# Determine and show the min and max values entered

read -p "n = " n
max=0
min=999999999999999999

while [ $n -ne -1 ]
do
	if [ $n -lt $min ]
	then
		min=$n
	fi
	if [ $n -gt $max ]
	then
		max=$n
	fi
	read -p "n = " n
done
echo "MIN = $min"
echo "MAX = $max"

