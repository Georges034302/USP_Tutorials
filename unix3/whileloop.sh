#!/bin/bash

# Read n from STDIN
# Show all values from 0 to n

echo -n "n = "
read n

i=0
while [ $i -lt $n ]
do
	echo $i
	((i++))
done
