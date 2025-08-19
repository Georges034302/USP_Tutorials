#!/bin/bash

# Read rain until -1
# Show the longest dry spell
# A dry spell is the number of days with no rain

read -p "rain = " rain
max=0
count=0

while [ $rain -ne -1 ]
do
	if [ $rain -eq 0 ]; then
		((count++))
	else
		max=$count
		count=0
	fi
	read -p "rain = " rain
done
if [ $max -lt $count ]; then
	max=$count
fi
echo "Longest dry spell = $max"
