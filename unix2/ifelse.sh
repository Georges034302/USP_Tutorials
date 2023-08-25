#!/bin/bash

# if-else syntax
#
# if [ <boolean expr> ]
# then
#	<code 1>
# else
#	<code 2>
# fi

# Req: Read an integer n from STDIN
# 	check if n is greater or equals to 10 or not
echo -n "n = "
read n

if [ $n -ge 10 ]
then
	echo "n >= 10"
else
	echo "n < 10"
fi

