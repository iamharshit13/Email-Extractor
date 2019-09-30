# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 14:33:57 2019

@author: harshit agrawal
github: iamharshit13
"""
#inporting Regular Expressions package
import re
#open first file in Read mode
rfile = open(input(str("Enter the location+name+extention of Readig file:")),"r")

#open 2nd file in Append mode
wfile = open(input(str("Enter the location+name+extention of Writing file:")),"a")

#loop for extracting data line by line
for line in rfile:
    line = line.rstrip()
    #here regular expression is used to extract mail id's from the data lines and it is a greedy operator
    email = re.findall('\S+@\S+', line)
    wfile.write(str(email)+"\n")


rfile.close()
wfile.close()
