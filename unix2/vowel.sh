#!/bin/bash
#write a script that reads characters from user until . is entered
#count the number of vowels entered.

echo -n "Character: "
read c 
count=0

while [ $c != "." ]
do
    #if [ $c = "a" ] || [ $c = "e" ] || [ $c = "i" ] || [ $c = "o" ] || [ $c = "u "]
    if [[ $c == [aeoiu] ]]   
    then
        ((count++))
    fi

    echo -n "Character: "
    read c 
done

echo "We entered $count vowels."
