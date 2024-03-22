#!/bin/bash

# Determine and show the longest dry spell
# A dry spell is a day with no rain
# Read rain until -1 then show the longest dry spell

read -p "Rainfall: " rain

count=0
max=0

while [ $rain -ne -1 ]
do
	if [ $rain -eq 0 ]
	then
		((count++))
	else
		if [ $max -lt $count ]
		then
			max=$count
		fi
		count=0
	fi
	read -p "Rainfall: " rain
done

if [ $max -lt $count ]
then
	max=$count
fi
echo "Longest dry spell = $max"

