#!/bin/bash

# Read direction from STDIN
# Check if the direction is N/S/E/W
# Anything else print incorrect direction

read -p "Direction (N/S/E/W): " d

case $d in
	N)
	echo "Go North on M1"
	;;
	S)
	echo "Go South on M5"
	;;
	E)
	echo "Go East on M8"
	;;
	W)
	echo "Go West on M4"
	;;
	*)
	echo "Incorrect Direction!"
	;;
esac


