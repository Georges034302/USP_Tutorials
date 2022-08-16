#!/bin/bash

#Create n-files where n is from STDIN
#File format: user-i.txt  (where 1 <= i <= n)

echo -n "How many files? "
read n

for((i=1;i<=$n;i++))
do
	touch $(whoami)-$i.txt
done

echo
echo "Verifying ..."
ls
echo
echo "cleaning ..."
rm $(whoami)*
ls
echo
