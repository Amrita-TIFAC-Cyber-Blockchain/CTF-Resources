plaintext="FLAG{Crypto_rocks}"

xorkey=1

ciphertext=""

for i in plaintext:
    ciphertext+=chr(ord(i)^xorkey)


print(ciphertext)
