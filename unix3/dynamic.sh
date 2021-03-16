#!/bin/bash

#Create a dynamic array of size n from argument
#Dynamic array is populated from user-input as the script runs

n=$1 #size of the array captured from argument

nums=() #creates an empty array

i=0

while [ $i -lt $n ]
do
    echo -n "Value: "
    read value

    nums[$i]=$value 
    
    ((i++))
done

echo
echo "Dymanic array: ${nums[@]}"
echo 

