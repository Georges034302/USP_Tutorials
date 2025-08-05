#!/bin/bash

echo "Welcome to Unix1"
echo
echo "User: $(whoami)"
echo
echo "Create a directory..."
mkdir sub1
cd sub1
echo "Create 5 files"
touch f{1..5}
cd ..
echo "Show sub1"
ls sub1
echo "Delete sub1"
rm -r sub1
echo "Thank you"
