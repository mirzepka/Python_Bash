#!/bin/bash

read num
if [[ $num > 20 ]] ;then 
echo $(lscpu |head -1)
fi

