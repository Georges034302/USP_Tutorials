#!/bin/bash

# capture first 2 arguments given to the script
# print each argument on a new line
# show the total number of arguments
# show the list of arguments
# show thefirst argument

var1=$1  # first arg
var2=$2  # second arg

echo $var1
echo $var2

echo "Total = $#"  		# how many arguments given
echo "List of Arguments: $@" 	# show the arguments
echo "First argument: $0" 

