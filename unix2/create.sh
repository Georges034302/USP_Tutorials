#!/bin/bash
#Create n-files formatted as: username<number>.txt
# 0<number<n
#n is passed to the script as argument

n=$1
echo "Creating $n files..."

for((i=0;i<$n;i++))
do
	touch $(whoami)$i.txt
done
ls -l

#for-loop
#for((i=1;i<=10;i++))
#do
#	echo $i
#done

#while-loop
#i=1
#while [ $i -le 10 ]
#do
#	echo $i
#	((i++))
	#repetition is required
#done
