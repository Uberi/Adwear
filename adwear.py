#!/usr/bin/env python3

import os, sys, time, random
import shutil, subprocess
import threading

if shutil.which("tmux") is None:
    print("NO TMUX PLS HALP")
    sys.exit(1)

sidebar_controller_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "sidebar_controller.py")
popup_controller_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "popup_controller.py")

def monitor():
    while True:
        os.system("tmux resize-pane -x 40 -t ADWEAR:0.1")
        time.sleep(0.5)
        if subprocess.check_output(["tmux", "list-panes", "-t", "ADWEAR:0"]).count(b"\n") < 2:
            os.system("tmux kill-session -t ADWEAR") # exit if the main terminal is closed
        time.sleep(0.5)

def popup():
    while True:
        time.sleep(random.randrange(10, 15))
        os.system("tmux new-window -k -t ADWEAR:1 -n POPUP")
        os.system("tmux send-keys '{}' C-m -t ADWEAR:1".format(popup_controller_path))
        time.sleep(random.randrange(8, 10))
        os.system("tmux kill-window -t ADWEAR:1")

os.system("tmux kill-session -t ADWEAR")
os.system("tmux new-session -d -s ADWEAR")
os.system("tmux split-window -h -t ADWEAR:0")
os.system("tmux send-keys '{}' C-m -t ADWEAR:0.1".format(sidebar_controller_path))
os.system("tmux select-pane -t ADWEAR:0.0")
os.system("tmux set-option status off") # turn off the bottom status bar
os.system("tmux set-option prefix 'C-@'") # change the prefix to a more obscure one
os.system("tmux set-option pane-border-fg white")
os.system("tmux set-option pane-active-border-fg white")
os.system("tmux set-option pane-active-border-bg default")

# set up monitoring thread
t = threading.Thread(target=monitor)
t.daemon = True # kill the monitor thread if the main thread exits
t.start()

# set up popup ads thread
t = threading.Thread(target=popup)
t.daemon = True # kill the monitor thread if the main thread exits
t.start()

os.system("tmux attach-session -t ADWEAR")

