#!/bin/bash
#read file content using cat
#file name is the first argument of the script

filename=$1

for line in `cat $filename`
do
	echo "$line"
done

