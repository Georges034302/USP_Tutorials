#!/bin/bash

# Get 2 integers from Arguments
# add, sub, multiply

result=$(($1+$2))
echo "$1 + $2 = $result"

result=$[ $1-$2 ]
echo "$1 - $2 = $result"

result=`expr $1 \* $2`
echo "$1 * $2 = $result"
