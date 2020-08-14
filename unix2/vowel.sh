#!/bin/bash
#Calculate the number of lowercase vowels from user-input until .

echo -n "Character: "
read c
count=0

while [ $c != "." ]
do
#	if [ $c = "a" ] || [ $c = "e" ] || [ $c = "i" ] || [ $c = "o" ] || [ $c = "u" ]
	if [[ $c = [aeiou] ]]
	then
		((count++))
	fi
	echo -n "Character: "
	read c
done
echo "Vowel count = $count"
