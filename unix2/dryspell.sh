#!/bin/bash
#Determine the longest dry spell

echo -n "Rainfall: "
read rain
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
			count=0
		fi
	fi
	echo -n "Rainfall: "
	read rain
done
if [ $max -lt $count ]
then
	max=$count
fi
echo "Longest dry spell = $max"
