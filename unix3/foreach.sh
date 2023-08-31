#!/bin/bash

#Req:
# Show each element in a sequence from start to end
# start to end are first and second arguments

echo -n "jump = "
read jump

for e in $(seq $1 $jump $2)
do
	echo $e
done

echo

for e in $(seq $1 $2)
do
	echo $e
done
