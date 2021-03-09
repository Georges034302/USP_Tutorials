#!/bin/bash

#Write a script that list of 10 numbers i and prints its power pow(i,i)

for ((i=1;i<=10;i++))
do
    pow=$(($i*$i))
    echo "$i --- $pow"
done





