#!/bin/bash

echo "Executing ..."

rm -r sub?

mkdir sub1 sub2

touch f1 f2 fa fb

mv f[0-9] sub1

mv f[a-z] sub2

ls -R

n=2

echo "$n+4 = $(($n+4))"

echo "Thank you!"

