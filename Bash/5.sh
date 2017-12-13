#!/bin/bash

pass="123"
coun=0

while [ $coun != 3 ]
do
    read typed
    if [[ $typed == $pass ]];then
        ls ../
        break
    fi
    ((coun++))
done

