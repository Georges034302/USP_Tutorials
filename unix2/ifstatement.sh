#!/bin/bash

# if-statement syntax

# if [ <logical expr> ]
#then
#	<code>
#fi

# Req: Read a name from STDIN
# Check if the name is george
# print welcome and then name
# print thank you

echo -n "Enter your name: "
read name

if [ $name == "george" ]
then
	echo "Welcome $name"
fi
echo "Thank you"
