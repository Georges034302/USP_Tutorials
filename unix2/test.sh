#!/bin/bash

file=unix2.txt

perm=$(stat -c %a "$file")

echo "Checking group permissions for $file"

[ $(($perm & 040)) ] &&	echo "readable"
[ $(($perm & 020)) ] && echo "writable"
[ $(($perm & 010)) ] && echo "executable"

echo -e "\nChecking others permission for $file"
[ $(($perm & 004)) ] && echo "readable"
[ $(($perm & 002)) ] && echo "writable"
[ $(($perm & 001)) ] && echo "executable"
