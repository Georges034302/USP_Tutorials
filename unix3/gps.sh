#!/bin/bash

# Enter a direction
# Select a NSW freeway
### Use a switch

PS3="Direction (N/S/E/W/x): "

select d in N S E W x
do
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
	x)
	exit
	;;
	*)
	echo "Incorrect direction!!!"
	;;
esac
done

