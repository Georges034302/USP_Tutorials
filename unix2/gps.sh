#!/bin/bash

# Read direction from STDIN
# Show the direction map

read -p " Direction: " d

case $d in
	N)
	echo "Go north on M1"
	;;
	S)
	echo "Go south on M2"
	;;
	E)
	echo "Go east on M5"
	;;
	W)
	echo "Go west on M4"
	;;
	*)
	echo "Unknown direction"
	;;
esac

