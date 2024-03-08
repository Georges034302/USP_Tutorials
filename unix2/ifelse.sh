#!/bin/bash

# enter integer from STDIN
# check if the value is greater than 10 or not

echo -n "n = "
read n

if [ $n -gt 10 ]
then
	echo "$n > 10"
else
	echo "$n <= 10"
fi
echo "Thank you"
