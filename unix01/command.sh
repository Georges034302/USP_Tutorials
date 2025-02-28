#!/bin/bash

mkdir sub
cd sub
touch f{1..4}
ls -l
cd ..
rm -r sub
ls
echo "Thank you!"
