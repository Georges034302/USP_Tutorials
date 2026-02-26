#!/bin/bash

# This is script 1:
# - Create a directory 'dir'
# - Create 3 files 
# - list the content of pwd
# - move all files to that directory
# - delete the directory

mkdir dir

touch f{1..3}

ls

mv f[0-9] dir

rm -r dir

