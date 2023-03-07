#!/bin/bash
#read charcaters until .
#show the total number of vowels lower-case

echo -n "Character: "
read c

count=0

while [ $c != "." ]
do
	if [[ $c == [aeiou] ]]
	then
		((count++))
	fi
	echo -n "Character: "
	read c
done
echo "Vowel count = $count"
