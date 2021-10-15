#!/usr/bin/python3

import sys
import os
import time
import random

arg = sys.argv[1]
print("Child with PID:", os.getpid(), " with argument:", arg, " has been started")
time.sleep(int(arg))
exit_status = random.randrange(0,2)
print("Process with PID:", os.getpid(), " has been finished")

os._exit(exit_status)
