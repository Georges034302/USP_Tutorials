#!/bin/bash
#write a script that determines the biggest number entered by user until -1

echo -n "Number: "
read num 

max=0

while [ $num -ne -1 ]
do
    if [ $num -gt $max ]
    then
        max=$num
    fi
    echo -n "Number: "
    read num 
done

echo "Max = $max"
echo
