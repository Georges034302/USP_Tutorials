#!/bin/bash

# Read direction from STDIN
# Check if the direction is N/S/E/W
# Anything else print incorrect direction
# Repeat the selection

PS3="Direction (N/S/E/W): "

select d in North South East West Exit
do
case $d in
	North)
	echo "Go North on M1"
	;;
	South)
	echo "Go South on M5"
	;;
	East)
	echo "Go East on M8"
	;;
	West)
	echo "Go West on M4"
	;;
	*)
	echo "Incorrect Direction!"
	break
	;;
esac

done
