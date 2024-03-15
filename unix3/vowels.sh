#!/bin/bash

# Read characters from STDIN until . is entered
# Count the number of vowels
# Show the vowel count

read -p "Character: " c

count=0
while [ $c != "." ]
do
	if [[ $c == [aeiou] ]]
	then
		((count++))
	fi
	read -p "Character: " c
done
echo "Vowel count = $count"
