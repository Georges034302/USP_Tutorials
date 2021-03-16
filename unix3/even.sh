#!/bin/bash

nums=(1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20)

length=${#nums[@]} #length of the array

echo "Even numbers: "

for((i=0;i<$length;i++))
do
    if [ $((${nums[$i]}%2)) == 0 ]
    then
        echo -n "${nums[$i]} "
        sum=$(($sum+${nums[$i]}))
    fi
done
echo 
echo "Even sum = $sum"
