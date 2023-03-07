#!/bin/bash
#display the first 3 arguments
#display the name of the script
#display the list of arguments

echo $1
echo $2
num=$3
echo $num
echo "script name: $0"
echo "arguments count = $#"
echo "arguments: $*"
