#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  1 22:22:31 2025

@author: mortivarus
"""
from pathlib import Path
import sys
import os

subreddits = Path("subreddits.txt")
subreddits_path = Path(__file__).parent

os.chdir(subreddits_path)

if subreddits.exists() == False:
    print("subreddits.txt does not exist.")
    
    sys.exit()

def read_file_to_list(file_path):
    lines = []
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            lines.append(line.rstrip('\n'))
    return lines

subreddits = sorted(
        list(
            set(
                read_file_to_list(subreddits)
                )
            )
        )

url = "www.old.reddit.com/r/"

for i in subreddits:
    url += f"{i}+"
    
if(url[-1] == "+"):
    url = url[:-1]

print(url)
