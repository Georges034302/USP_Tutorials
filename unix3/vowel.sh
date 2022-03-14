#!/bin/bash
#Count the number of vowels entered from STDIN until .

echo -n "Letter: "
read c

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
