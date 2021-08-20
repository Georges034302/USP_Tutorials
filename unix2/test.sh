#!/bin/bash

#create 3 files f1 f2 f3
#display long all files
#change permission: user full previliges, group nothing, othercan execute
#display long all files
#remove all files

touch f1 f2 f3
ls -l
chmod 701 f[0-9]
ls -l
rm f[0-9]  #rm f*  would delete all files starting with f, for example: f3333 fdd44, ..
