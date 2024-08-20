#!/bin/bash

# Enter a direction from STDIN
# Determine the road based on N,S,E,W
# Anything else it should say incorrect direction

read -p "Direction (N/S/E/W): " d

case $d in
	N)
	echo "Going north on M1"
	;;
	S)
	echo "Going south on M7"
	;;
	E)
	echo "Going east on M5"
	;;
	W)
	echo "Going west on M4"
	;;
	*)
	echo "Incorrect direction!"
	;;
esac
