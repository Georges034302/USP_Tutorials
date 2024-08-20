#!/bin/bash

# This is my first script
echo "Creating files..."
touch f{1..5}

echo "Creating directory..."
mkdir sub

echo "Move all files to sub..."
mv f? sub

echo "List sub contents..."
ls sub

echo "Delete sub..."
rm -r sub
