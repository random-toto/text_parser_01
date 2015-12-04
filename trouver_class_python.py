#!/usr/bin/python3
#-*- coding: utf-8 -*-


################################################################################
import os
import re


f = input("fichier de classes ? ")
CLASS = re.compile('^class')
RAZ = re.compile('(^\S)|(^( )*\n)')


cls = False
with open(f, 'r') as fr:
    for i, line in enumerate(fr):
        if RAZ.findall(line):
            if cls:
                cls = False
                print()
        if CLASS.findall(line):
            cls = True
        if cls:
            print(line, end='')
        

