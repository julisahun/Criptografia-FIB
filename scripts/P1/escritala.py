import sys
import time

text = open('text.txt').read()

def encrypt(rows, plaintext):
    assert len(plaintext) % rows == 0
    n = len(plaintext)
    columns = n // rows
    ciphertext = ['-'] * n
    for i in range(n):
        row = i // columns
        col = i % columns
        ciphertext[col * rows + row] = plaintext[i]
    return "".join(ciphertext)

def decrypt(rows, ciphertext):
    while len(ciphertext) % rows != 0:
        ciphertext += '-'
    return encrypt(len(ciphertext) // rows, ciphertext)

for i in range(50, 200):
    if len(sys.argv) > 1: 
        i = int(sys.argv[1])
        print(decrypt(i,text))
        exit()
    decrypted = decrypt(i, text)
    if i%100 == 0:
        print('-------', i, '-------')
    if decrypted.count('the') > 500:
        print(i, decrypted.count('the'))
        time.sleep(0.2)