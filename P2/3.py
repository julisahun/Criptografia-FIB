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


ciphertext = open("./files/" + name + "/AES_juli.sahun_2022_09_20_16_59_27.puerta_trasera.enc", "rb").read()
chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
key = {}
for char1 in chars:
    for char2 in chars:
        key[0] = list(map(ord, char1*8 + char2*8))
        for char3 in chars:
            for char4 in chars:
                key[1] = list(map(ord, char3*8 + char4*8))
                for char5 in chars:
                    for char6 in chars:
                        key[2] = list(map(ord, char5*8 + char6*8))
                        for char7 in chars:
                            for char8 in chars:
                                key[3] = list(map(ord, char7*8 + char8*8))
                                for char9 in chars:
                                    for char10 in chars:
                                        key[4] = list(map(ord, char9*8 + char10*8))
                                        for char11 in chars:
                                            for char12 in chars:
                                                key[5] = list(map(ord, char11*8 + char12*8))
                                                for char13 in chars:
                                                    for char14 in chars:
                                                        key[6] = list(map(ord, char13*8 + char14*8))
                                                        for char15 in chars:
                                                            for char16 in chars:
                                                                key[7] = list(map(ord, char15*8 + char16*8))
                                                                masterKey = functools.reduce(listXor, key.values())
                                                                h = hashlib.sha256(toBinary(masterKey)).hexdigest()
                                                                finalKey = str.encode(h[:16])
                                                                iv = str.encode(h[48:])

                                                                cipher = AES.new(finalKey, AES.MODE_CBC, iv)
                                                                pt = cipher.decrypt(ciphertext)
                                                                if filetype.guess(pt) != None:
                                                                    print(filetype.guess(pt))
                                                                    exit()
            



