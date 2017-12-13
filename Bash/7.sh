#!/bin/bash
echo "Podaj dzialanie, ex. 2+2"
exp=""
while [[ $exp != "quit" ]]
do
read exp
echo "$exp = $((exp))"
done
