#!/bin/bash
# use IFS to read file content

while IFS= read -r line;do
	echo $line
done < "$1"
