#!/bin/bash

#if-statement syntax:
#
# if [ <boolean expr> ]
# then
#	<code>
# fi

#Req: Read a name from STDIN
#	show the name if it is Tom

echo -n "Name: "
read name

if [ $name == "Tom" ]
then
	echo "Welcome $name"
fi
echo "Good bye"
