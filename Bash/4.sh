#!/bin/bash
pass="123"

read typed
if [[ $typed == $pass ]];then
    echo "Correct password"
else
    echo "Wrong password"
fi

