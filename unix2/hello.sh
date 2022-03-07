#!/bin/bash
#Read a name from STDIN
#Display the name on the screen
#Show the age passed to the script as argument
#Show the number of arguments
#Show the list of arguments

echo -n "Enter your name: "
read var

echo "Welcome $var your age is $1"
echo "executing $0"
echo "We entered $# arguments"
echo "The arguments are: $*"
