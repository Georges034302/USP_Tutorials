#!/bin/bash

echo "Clean up directory ..."
rm f?
rm -r sub?

echo "Creating 5 files ..."
touch f{1..5}

echo "Creating directory ..."
mkdir sub1

echo "Moving all files to sub1 ..."
mv f? sub1

echo "Verify script output ..."
ls sub1
