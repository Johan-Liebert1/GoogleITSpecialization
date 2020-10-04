#!/usr/bin/env python3

import sys, subprocess

# oldFiles.txt is supposed to be the first command line argument

old_files = sys.argv[1]
prepend = '/home/student-01-146e704cd9e1'
with open(old_files) as file:
    for line in file.readlines():
        # strip() to remove new_line character
        new_filename = line.strip().replace("jane", "jdoe")

        subprocess.run(['mv', prepend + line.strip(), prepend + new_filename])