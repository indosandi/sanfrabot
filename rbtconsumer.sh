#!/bin/bash
sh setup.sh
nohup python main.py rbtconsumer $1 > out.main &
