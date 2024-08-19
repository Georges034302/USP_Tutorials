#!/bin/bash

# Read a direction from STDIN and determine the  road

read -p "Direction(N/S/E/W): " d

case $d in
	N)
	echo "Going north on harbor bridge"
	;;
	S)
	echo "Going south on M7"
	;;
	E)
	echo "Going east on M1"
	;;
	W)
	echo "Going west on M4"
	;;
	*)
	echo "Incorrect direction"
	;;
esac

