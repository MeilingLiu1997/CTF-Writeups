# [WolvCTF 2025](https://wolvctf.io/)

---

# Beginner
## REverse
Resource: 
- [./reverse](beginner/reverse)
- `out.txt`
```
Mixed Flag: t`qcxo0s0o2.kd\.k\o0s0o20z
```

### Solution
[reverse.c](beginner/reverse.c)
flag: wctf{r3v3r51ng_1n_r3v3r53}


## REdata - Rev
strings ./redata
flag: wctf{n0_w4y_y0u_f0unD_1t!}

## OverAndOver - Crypto
encoded.txt
do multiple base64 decode

## EtTuCaesar - Crypto
message.txt
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

flag: wctf{v3n!_V!dI_v!C!_!1!1}


## JWT Learning - Web
tool: https://jwt.io/
encoded: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6InNhbSIsImlzQWRtaW4iOnRydWUsImlhdCI6MTc0MjY3NDc5OCwiZXhwIjoxNzQyNjkyNzk4fQ.c7tgVr9B0n3OUfzYe2mSXr_s1R0_mdlvAnNBWqGhXRk
decoded:
	header:
	{
	  "alg": "HS256",
	  "typ": "JWT"
	}
	payload:
	{
	  "username": "sam",
	  "isAdmin": true,
	  "iat": 1742674798,
	  "exp": 1742692798
	}

hints from : https://beginner-jwt-learning-974780027560.us-east5.run.app/robots.txt
![alt text](beginner/jwt1.png)

go to https://beginner-jwt-learning-974780027560.us-east5.run.app/TOKEN_SECRET.txt
find: fa43623fc456bf3a62ea923f4e7a009f0aeec4a0032670ed6fc90bd268e4c62c896699572b914cb15806695fcb1f6eb3141c9bc86a87cca1bda98e1429aa902b
![alt text](beginner/jwt2.png)

set this key to VERIFY SIGNATURE window in https://jwt.io/
now: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6InNhbSIsImlzQWRtaW4iOnRydWUsImlhdCI6MTc0MjY3NDc5OCwiZXhwIjoxNzQyNjkyNzk4fQ.c7tgVr9B0n3OUfzYe2mSXr_s1R0_mdlvAnNBWqGhXRk

change cookies and go to https://beginner-jwt-learning-974780027560.us-east5.run.app/get-flag
![alt text](beginner/jwt3.png)
flag:wctf{jw7_l34rn1n6_15_fun_135624154}


## PicturePerfect - Forensics
Resource: 
- hi_snowman.png

![alt text](beginner/snow.png)
see title: wctf{d0_yOU_w@nt_t0_BUiLd_a_Sn0Wm@n}

## DigginDir - Forensics
Resource: challenge/
![alt text](beginner/diggindir.png)
flag: wctf{0h_WOW_tH@Nk5_yOu_f0U^d_1t_xD}

## p0wn3d - Pwn
flag: wctf{pwn_1s_l0v3_pwn_1s_l1f3}

## p0wn3d - Pwn
flag: wctf{4ll_y0uR_mEm_4r3_bel0ng_2_Us}

## p0wn3d_3 - Pwn
flag: wctf{gr4dua73d_fr0m_l1ttl3_p0wn3r!}


---

# Misc
## Eval is Evil
Resource: 
- Eval is Evil/chall.py

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

![alt text]("Eval is Evil"/eval.png)

flag: wctf{Why_Gu3ss_Wh3n_Y0u_C4n_CH34T}


---

# Forensics
## Passwords
Resource: 
- Database.kdbx (keepass with password)

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
Resource: 
- js/

In js/app.js, req.query.username can be an object or array, leading to unexpected behavior. If an error occurs, the app serves flag.txt, which may expose sensitive information.

### Test out
https://js-puzzle-974780027560.us-east5.run.app/?username[]=test
![alt text](pass1.png)

### Solution
https://js-puzzle-974780027560.us-east5.run.app/?username[toString]=fail
![alt text](pass2.png)

flag: wctf{3xc3pt10n5_4r3_y0ur_fr13nd_14285137553}