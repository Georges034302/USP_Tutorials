#!/bin/bash

# Welcome the system user
echo "Welcome $(whoami)"

# Read the user role from STDIN and show it to STDOUT
echo -n "Enter your role: "
read role
echo "Your role is $role"

echo "Your salary is $1"
echo "Your location is $2"
echo "Running script: $0"
