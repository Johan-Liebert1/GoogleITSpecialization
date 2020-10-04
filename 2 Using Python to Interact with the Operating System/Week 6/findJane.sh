#!/bin/bash

> oldFiles.txt

grep " jane " ../data/list.txt | cut -d ' ' -f 3 >> oldFiles.txt
