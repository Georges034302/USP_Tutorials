#!/bin/bash

#Req:
# Show the current system user
# Show the  PID running under this user account
# NOTE: you must use functions

function show(){
	echo "User: $(whoami)"
	ps aux | awk '{print $2}'
}

show
