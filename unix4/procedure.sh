#!/bin/bash

# A procedure is an action method
# A proceddure is always a verb
# A procedure does something but does not return a value

# Show the current user
# Show the PID of all processes

function show(){
	echo "User: $(whoami)"
	ps aux | awk '{print $2}'
}

show
show
show
show
