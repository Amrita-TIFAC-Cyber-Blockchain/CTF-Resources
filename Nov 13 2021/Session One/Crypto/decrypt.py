ciphertext="GM@FzBsxqun^snbjr|"  #This is cipher

plaintext="FLAG{"     #This is plain text

#key=plaintext^ciphertext
value=[]                    
for i in range(len(plaintext)):
    value.append(ord(plaintext[i])^ord(ciphertext[i]))
    print(value)


key=1

flag=""
for i in ciphertext:
    flag+=chr(ord(i)^key)

print(flag)


#bruteforce

for i in range(0,255):
    for j in range(len(plaintext)):
        if(chr(i^ord(plaintext[j])))==ciphertext[j]:
            print("found")
            print(i)
            print(plaintext[j])
            print("------------------------------------")
