#!/bin/bash
for (( i=1; i<=30; i++ ))
do
   nohup python main.py rbtconsumer $i > out.main &
   echo "$i"
   sleep 1
done
