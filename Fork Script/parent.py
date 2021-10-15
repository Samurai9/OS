#!/usr/bin/python3

import os
import sys
import random


childs_count = int(sys.argv[1])

for i in range (0, childs_count):
	pid = os.fork()
	if (not pid):
		rand_num = random.randint(5,10)
		os.execl("./child.py", "child.py", str(rand_num))

for i in range (0, childs_count):
	child_info = os.wait()
	print("Child process with PID:", child_info[0], " has been finished. Exit status:", child_info[1])
