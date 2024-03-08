#!/bin/bash

echo "Creating 5 files ..."
touch f{1..5}

echo "Creating directory ..."
mkdir sub1

echo "Moving files to directory ..."
mv f? sub1

echo "Listing directory ..."
ls sub1

echo "Clean up folder ..."
rm -r sub1

echo "Thank you "
