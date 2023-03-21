#!/bin/bash
#Convert IPv4 to Binary IP
#IPv4 example:192.168.23.1
#Binary IP example: 11001000.10101010.11111101.01000100
#For any given IP from argument, conver the IP to binary
#To simply, represent the IP by first 4 integer arguments

echo "IPv4: $1.$2.$3.$4"
ip=($1 $2 $3 $4)

function convert(){
	zeros=(0 0 0 0 0 0 0 0)
	array=()
	number="${1}" #one decimal value argument
	for((i=0;i<${#zeros[@]};i++))
	do
		array[$i]=$(($number%2)) #0 or 1
		number=$((number/2)) #update number
	done

	binary=()
	j=0
	for((i=0;i<${#array[@]};i++))
	do
		binary[$j]=${array[$i]}
		((j++))
	done
	echo "${binary[@]}"
}

r1=$(convert $1)
r2=$(convert $2)
r3=$(convert $3)
r4=$(convert $4)

echo "Binary IP: $r1.$r2.$r3.$r4"
