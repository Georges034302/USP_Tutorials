#!/bin/bash

echo -n "Name: "
read name

if [ $name == "Tom" ]
then
	echo "Welcome $name"
fi
echo "Good bye!"
