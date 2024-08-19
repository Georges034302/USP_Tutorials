#!/bin/bash

# My first script
echo "Creating 5 files..."
touch f{1..5}

echo "Creating a directory ..."
mkdir sub

echo "Moving files to sub..."
mv f? sub

echo "List sub contents..."
ls sub

echo "Deleting sub..."
rm -r sub
