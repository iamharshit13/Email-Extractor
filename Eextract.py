# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 14:33:57 2019

@author: harshit agrawal
github: iamharshit13
"""

import re

rfile = open(input(str("Enter the location+name+extention of Readig file:")),"r")
wfile = open(input(str("Enter the location+name+extention of Writing file:")),"a")
for line in rfile:
    line = line.rstrip()
    email = re.findall('\S+@\S+', line)
    wfile.write(str(email)+"\n")


rfile.close()
wfile.close()