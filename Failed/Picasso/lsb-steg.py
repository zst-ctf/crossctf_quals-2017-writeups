'''
#! /usr/bin/env python3
for iter in range(16):
    with open("picaso.png", "rb") as file:
        data = file.read()
        data = data[iter:]

        bits = ""
        for c in data:
            lsb = str(c & 0x1)
            bits += lsb

        bytess = [chr(int(bits[i:i+8], 2)) for i in range(0, len(bits), 8)]
        lsbstr = "".join(bytess)
        print(lsbstr)
        if "ross" in lsbstr:
            break
'''
