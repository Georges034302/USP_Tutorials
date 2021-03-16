#!/bin/bash
#Create a sequential array that starts and ends with argument values
#iterate using an argument value as well.
start=$1
jump=$2
end=$3

nums=($(seq $start $jump $end))

length=${#nums[@]} #length of the array

echo "Sequential array: ${nums[@]}"
echo -n "Even numbers: "

for e in ${nums[@]}
do
    if [ $(($e%2)) == 0 ]
    then
        echo -n "$e "
        sum=$(($sum+$e))
    fi
done
echo 
echo "Even sum = $sum"

average=$(echo "scale=5;$sum/$length" | bc)

echo "Even average = $average"
echo
