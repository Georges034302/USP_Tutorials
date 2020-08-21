#!/bin/bash

ls -l | tail -n+2 $1

cat $1 | awk '{printf "%10s %4d %-8s \n",$1,$5,$9}'

wc $1
