#!/bin/bash

#Write a script that checks if a word is a file or a directory

if [ -d $1 ]
then
    echo "$1 is a directory."
elif [ -f $1 ]
then
    echo "$1 is a file."
else
    echo "$1 does not exist!!!!!!!"
fi

