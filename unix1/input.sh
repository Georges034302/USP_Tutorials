#!/bin/bash

# Enter a and b and show the total, sub, div, mul

echo -n "a = "
read a

read -p "b = " b

echo $(($a+$b))
echo $(($a-$b))
echo $(($a*$b))
echo $(($a/$b))
