#!/bin/bash
#Create n-files sequentially using touch
#n is the number of files passed as argument
#If the script runs again, it should create files
#from the last file number + 1
#The file name should be formatted as: <username>-<number>.txt
#NOTE: <username>-0.txt should be labelled <username>.txt

n=$1
echo "Creating $ files ..."

first=1

while true
do
	if [ -e $(whoami)$first.txt ]
	then
		((first++))
	else
		break
	fi
done

for((i=$first-1;i<$(($first+$n));i++))
do
	if [ $i -eq 0 ]
	then
		touch $(whoami).txt
	else
		touch $(whoami)$i.txt
	fi
done
ls -l
