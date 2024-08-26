#!/bin/bash

# Read a charcater until .
# Show the total number of vowels entered

read -p "Character: " c
count=0

while [ $c != "." ]
do

	if [[ $c == [aieouAEIOU] ]]
	then
		((count++)) #count=$(($count+1))
	fi
	read -p"Character: " c
done

echo "Total vowels = $count"
