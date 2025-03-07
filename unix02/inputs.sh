#!/bin/bash

# Read two values from STDIN
# Show the total

echo -n "a = "
read a

read -p "b = " b

result=$(($a+$b))
echo "Total = $result"

# Multiply the total by first integer argument
total=$(($result*$1))
echo "Total multiplication = $total"
