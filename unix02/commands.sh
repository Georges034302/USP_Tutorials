#!/bin/bash

echo "Bash scripting lesson:"

echo
mkdir sub
cd sub
pwd
touch f{1..3}
ls -l
chmod 777 f[0-9]
ls -l
cd ..
rm -r sub
ls
echo "Thank you"
