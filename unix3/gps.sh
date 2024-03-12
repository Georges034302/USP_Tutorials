#!/bin/bash

# Read direction from STDIN
# Select the correct freeway

PS3="Direction: "

select d in N S E W x
do
case $d in
	N)
	echo "Go North over the Harbor Bridge"
	;;
	S)
	echo "Go to South Sydney via M5"
	;;
	E)
	echo "Go to Eastern Suburbs via M1"
	;;
	W)
	echo "Go to Western Suburbs via M4"
	;;
	x)
	exit
	;;
	*)
	echo "Incorrect direction"
	;;
esac
done
