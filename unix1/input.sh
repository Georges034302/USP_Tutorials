#!/bin/bash

# Read username from STDIN
# Say hello

echo -n "Enter your name: "
read name
echo "Hello $name"

# Read the role
read -p "My role: " role
echo "My role is: $role"
