#!/bin/bash

# Show the current user and print the PID

function show_user(){
	echo "User --> $(whoami)"
	ps aux | awk '{print $2}'
}

show_user
show_user
