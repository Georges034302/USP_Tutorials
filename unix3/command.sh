#!/bin/bash

ls -l | tail -n+2

cat $1 | awk '{printf "%6s %4d %10s \n",$3,$5,$9}'

wc $1
