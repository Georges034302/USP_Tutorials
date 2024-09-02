#!/bin/bash

# Procedure:
# - verb
# - Does not return a value
# - Action that does something

# Define a procedure to do the following:
# - Show the current system user
# - Identify the CPU processes and only show the jobs
# containing linux (show the PID and command)

function show(){
	echo "System user: $(whoami)"
	ps aux | awk '{printf"%6s %20s\n",$2,$11}' | grep -i 'linux'
}

show
show
show
show
