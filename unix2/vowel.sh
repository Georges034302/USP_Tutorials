#!/bin/bash

#Read letters from STDIN until .
#Count the number of lowercase vowels

echo -n "Letter: "
read c

count=0

while [ $c != "." ]
do
	if [[ $c == [aioeu] ]]
	then
		((count++))
	fi

	echo -n "Letter: "
	read c
done

echo "Vowel count = $count"
