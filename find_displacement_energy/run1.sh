#!/bin/bash

ncell=5
counter=1
drname=0.1
while [  $counter -le $ncell ]; do
    cd $drname
         mpirun -np 32 /home/iyad/vasp.5.4.4/bin/vasp_std

    cd ../
    (( counter=$counter+1 ))
    drname=$(awk -v drname="$drname" 'BEGIN{printf "%.1f", drname+0.1}')
done

