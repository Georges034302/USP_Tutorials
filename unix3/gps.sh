#!/bin/bash

# Enter a direction from STDIN
# Determine the road based on N,S,E,W
# Anything else it should say incorrect direction

PS3="Direction (N/S/E/W): " # prompt

select d in North South East West Exit
do
   case $d in
	North)
	echo "Going north on M1"
	;;
	South)
	echo "Going south on M7"
	;;
	East)
	echo "Going east on M5"
	;;
	West)
	echo "Going west on M4"
	;;
	Exit)
	break
	;;
	*)
	echo "Incorrect direction!"
	;;
   esac
done
