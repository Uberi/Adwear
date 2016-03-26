#!/usr/bin/env python3

import os

def initialize_session():
    os.system("tmux new-session -s ADWEAR") # -d for a new terminal rather than taking over the current one
    os.system("tmux new-window -t ADWEAR:1")

initialize_session()