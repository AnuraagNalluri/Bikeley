import time
import os
import subprocess
from subprocess import *
def loop():
    # import testhtml
    subprocess.call('python testhtml.py', shell=True, cwd='/Users/shiva/desktop/bikeley')
while True:
    loop()
    time.sleep(1)
