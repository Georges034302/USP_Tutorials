#!/bin/bash
# if-else syntax

# if [ <boolean expr> ]
# then
#	<code 1>
# else
#	<code 2>
# fi
# Req: read an integer n from STDIN
# check if the n is greater than 10
# print n > 10
# Othwwise print n <= 10

echo -n "n = "
read n

if [ $n -gt 10 ]
then
	echo "n > 10"
else
	echo "n <= 10"
fi
