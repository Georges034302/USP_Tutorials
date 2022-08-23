#!/bin/bash

ls -l | tail -n+2 | awk '{printf "%s %-5d %-15s\n",$3, $5, $9}'



