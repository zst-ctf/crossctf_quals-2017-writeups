#!/usr/bin/env python
from base64 import b64decode 
import sys

with open("godeep_5b4a789794a6d5fba439db1fde186765.txt", "r") as file:
    input = file.read().strip()

iter = 0
while "CrossCTF" not in input:
    input = input.strip()

    try: # hex decode
        input = input.decode("hex").strip()
    except: # if not, should be base64
        input = b64decode(input).strip()
    
    iter += 1

print "iter = ", iter
print input