#!/bin/bash

a=2
b=5

result1=$(($a+$b))
echo "a + b = $result1"

result2=$[ $a+$b ]
echo "a + b = $result2"

result3=`expr $a + $b`
echo "a + b = $result3"
