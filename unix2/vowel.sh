#!/bin/bash
#Count the lowercase vowels from user input until .

echo -n "Character: "
read c

while [ $c != "." ]
do
#	if [ $c = "a" ] || [ $c = "e" ] || [ $c = "i" ] || [ $c = "o" ] || [ $c = "u" ]
	if [[ $c = [aeiou] ]]
	then
		((count++))
	fi
	echo -n "Charcater: "
	read c
done

echo "Vowel count = $count"
