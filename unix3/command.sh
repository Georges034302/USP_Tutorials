#!/bin/bash

ps aux | awk '{printf "%-15s %-10s %-20s \n",$1,$2,$11}'
