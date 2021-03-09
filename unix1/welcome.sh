#!/bin/bash
#Enter your name 
#Save it to a variable
#The print the welcome message

echo -n "Enter your name: "
read name

echo "Hi $name, Welcome to USP 32547"
echo "Your mark is $1 and grade is $2"

echo "Running $0"
echo "This script has $*"

echo "Number of arguments is $#"

