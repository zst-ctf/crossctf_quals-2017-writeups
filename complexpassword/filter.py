#!/usr/bin/env python
import re

REGEX = r'''^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[~!@#\$%\^&*_\-\+=`|\\\(\)\{\}\[\]:;"'<>,\.\?/]).+$'''
# REGEX = r'''^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[~!@#\$%\^&*_\-\+=`|\\\(\)\{\}\[\]:;"'<>,\.\?/]).{25,}$'''

def isMatch(string):
    return re.compile(REGEX).match(string)

with open("10m_passwords_307225a24bea70813d6218f4faf64780", "r") as file:
    input = file.read()

for line in input.split("\n"):
    if isMatch(line):
        print line