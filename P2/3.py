from doctest import master
from pydoc import plain
from Crypto.Cipher import AES
import functools
import filetype
import hashlib

name = "juli"

ciphertext = open("./files/" + name + "/AES_juli.sahun_2022_09_29_11_10_34.enc", "rb").read()

key = open("./files/" + name + "/AES_juli.sahun_2022_09_29_11_10_34.key", "rb").read()

iv = open("./files/" + name + "/AES_juli.sahun_2022_09_29_11_10_34.iv", "rb").read()

cipher = AES.new(key, AES.MODE_CBC, iv)
pt = cipher.decrypt(ciphertext)
print(filetype.guess(pt))


# b


def listXor(a, b):
    ret = []
    for i in range(len(a)):
        ret.append(a[i] ^ b[i])
    return ret

def toBinary(list):
    ret = bytearray()
    for i in list:
        ret.append(i)
    return bytes(ret)

def pad(key):
    ret = bytearray(key)
    p = 16 - len(ret) or 16
    for i in range(p):
        ret.append(p)
    return bytes(ret)


ciphertext = open("./files/" + name + "/AES_juli.sahun_2022_09_20_16_59_27.puerta_trasera.enc", "rb").read()
files = {}
for i in range(256):
    print(i)
    for j in range(256):
        h = hashlib.sha256(toBinary([i,i,i,i,i,i,i,i,j,j,j,j,j,j,j,j])).hexdigest()
        finalKey = pad(str.encode(h[:16]))

        iv = str.encode(h[48:])

        cipher = AES.new(finalKey, AES.MODE_CBC, iv)
        pt = cipher.decrypt(ciphertext)
        if filetype.guess(pt) != None:
            print(filetype.guess(pt))
            if filetype.guess(pt) not in files:
                files[filetype.guess(pt)] = []
            files[filetype.guess(pt)].append(pt)
                                                                   
            



