#!/bin/bash

# check if the name is George
# Welcome George
# finish with Goodbye

#Use single-if to compelete the task:
# if [condition]
#then
# 	<code>
#fi

echo -n "Name: "
read name

if [ $name == "George" ]
then
	echo "Welcome $name"
fi
echo "Goodbye"


