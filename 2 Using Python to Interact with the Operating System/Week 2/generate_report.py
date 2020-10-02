import os
import subprocess

os.system('rm hello.txt')

subprocess.run(['touch', 'new_hello.txt'])



