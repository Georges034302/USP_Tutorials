#!/bin/bash

#Write a script that shows the first three arguments
#Then show the name of the executed script
#Then show the total number of arguments passed to the script
#Then show the arguemts list

echo $1
echo $2
echo $3
echo
echo "Script name: $0"
echo
echo "Number of arguments: $#"
echo
echo "List of arguments: $*"


