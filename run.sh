#!/bin/bash

if [ -z "$1" ]
then
        sed -e "s|output.nc|${USER}/output.nc|" namelist.pamm > namelist.tmp
else
        sed -e "s|output.nc|${USER}/output.nc|" $1 > namelist.tmp
fi



mkdir /tmp/${USER}
./main.exe namelist.tmp
rm namelist.tmp 



