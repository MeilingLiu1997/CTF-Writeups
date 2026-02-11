text = "lactf{REDACTED}"
endian = text.encode(encoding="utf-16le").decode(encoding="utf-8")
with open("chall.txt", "wb") as file:
    file.write(endian.encode())