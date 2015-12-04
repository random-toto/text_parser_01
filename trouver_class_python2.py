#!/usr/bin/python3
#-*- coding: utf-8 -*-


################################################################################
import os
import re


f = input("fichier de classes ? ")
CLASS = re.compile('^class')
RAZ = re.compile('(^\S)|(^( )*\n)')


m = []
l = []
cls = False
with open(f, 'r') as fr:
    for i, line in enumerate(fr):
        if RAZ.findall(line):
            if cls:
                cls = False
                m.append(l)
        if CLASS.findall(line):
            cls = True
            l = []
        if cls:
            l.append(line)


