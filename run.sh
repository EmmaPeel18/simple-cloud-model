#!/bin/bash

sed -e "s|output.nc|${USER}/output.nc|" namelist.pamm > namelist.tmp

mkdir /tmp/${USER}
./main.exe namelist.tmp
rm namelist.tmp 



