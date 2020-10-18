#!/bin/bash
# Launch pinbot

tmux new -ds pinbot "python3 bot.py 2>&1 | tee log.txt"

