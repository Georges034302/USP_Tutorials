#!/bin/bash
#read a word from argument
#determine if this word is a file or a directory or it does not exist!

if [ -d $1 ]
then
    echo "$1 is a directory"
elif [ -f $1 ]
then
    echo "$1 is a file"
else
    echo "$1 does not exist!!!"
fi

