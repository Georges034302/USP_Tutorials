#!/bin/bash

echo -n "Enter your name: "
read name
echo "Welcome $name"

read -p "Enter your age: " age
echo "$name age is $age"

role=$1
echo "$name role is: $role"
