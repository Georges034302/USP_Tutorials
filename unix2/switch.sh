#!/bin/bash

# Enter a direction
# Select a NSW freeway
### Use a switch

read -p "Direction (N/S/E/W): " d

case $d in
	N)
	echo "Going north over the harbor bridge"
	;;
	S)
	echo "Going south on the M5"
	;;
	E)
	echo "Going to Eastern suburbs on M1"
	;;
	W)
	echo "Going to west Sydney on M4"
	;;
	*)
	echo "Incorrect direction!!!"
	;;
esac


