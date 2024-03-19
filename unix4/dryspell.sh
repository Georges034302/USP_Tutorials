#!/bin/bash

# Determine the longest dry spell
# A dry spell is the number of days with no rain
# Longest dry spell = max no rain days
# Read rain until -1, then show longest dry spell

read -p "Rainfall: " rain

max=0
count=0

while [ $rain -ne -1 ]
do
	if [ $rain -eq 0 ]
	then
		((count++))
	else
		if [ $count -gt $max ]
		then
			max=$count
		fi
		count=0
	fi
	read -p "Rainfall: " rain
done
if [ $count -gt $max ]
then
	max=$count
fi
echo "Longest dry spell = $max"
