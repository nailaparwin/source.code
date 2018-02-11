#!/bin/bash

ncell=10

counter=1
while [  $counter -le $ncell ]; do
    mkdir $counter

    cp ../$counter/OUTCAR ./$counter/

    (( counter=$counter+1 ))
done                                                                                    
