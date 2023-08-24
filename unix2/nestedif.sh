#!/bin/bash

#nested-if example syntax:

# if [ <boolean expr> ]
# then
# 	<code 1>
#	if [ <boolean expr> ]
#	then
#		<code 2>
#	else
#		<code 3>
#	fi
# else
#
#	<code 4>
# fi
#Req: Read an integer n from STDIN
#     check if n is positive or zero
#     	check if n is even
#	or if n is odd
#     othwise print n is negative

read -p "n = " n

# echo -n "n = "
# read n

if [ $n -ge 0 ]
then
	if [ $(($n%2)) == 0 ]
	then
		echo "$n is even"
	else
		echo "$n is odd"
	fi
else
	echo "$n is negative"
fi















