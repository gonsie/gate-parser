#!/bin/bash

# make 'current' dir if it doesn't exist
if [ ! -e current/ ]; then
    mkdir current
    mkdir current/old
else
    if [ ! -e current/old ]; then
        mkdir current/old
    fi
    mv current/*.* current/old/
fi

# read file name from command line
echo -n "Library File: "
read flib
if [ ! -e $flib ]; then
    echo $flib does not exist
    exit 1
fi

echo -n "Netlist File: "
read fnet
if [ ! -e $fnet ]; then
    echo $fnet does not exist
    exit 1
fi

# pass along to parser system
./full_parser.py $flib $fnet

# generate C code
fnet=${fnet##*/}
fnet=${fnet%.*}
cat current/${fnet}_gates.txt | sort -n > current/${fnet}_gates_sort.txt
