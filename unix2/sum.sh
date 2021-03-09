#!/bin/bash
#Write a script that adds all integers entered by user until -1

echo -n "Number: "
read num 

sum=0

while [ $num -ne -1 ]
do
    # let sum=$sum+$num
    sum=$(($sum+$num))

    echo -n "Number: "
    read num  
done

echo "Sum = $sum"
echo
