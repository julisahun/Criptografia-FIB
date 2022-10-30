from itertools import product
from Crypto.PublicKey import RSA
import sympy

# key_encoded='''-----BEGIN PUBLIC KEY-----
# MIIBITANBgkqhkiG9w0BAQEFAAOCAQ4AMIIBCQKCAQByM12PLgtaKidKoXwNWXZO
# 6PhiNKqTU9yUYv81WkTxdn09+reugyUJ7ZIZGQAfWVszAuIgiaMb6/Dl8NRFx754
# oGIMs+37xeVS36RbpAehgJuEm6SmX3NEA4liLipInux8bBlRjxZG68BA/PsVp1W0
# 18zkYft2bFf2FvghXdOy9UDo5s5aO+mqcwxcm2xzJhIQ916BP6I9rcfvId0mfzQg
# JU/0iaLp/F8SkpPdmn2YFY7KV0P7qSX+22hsnJMZExQIPdHhs9hH9PA0qfWYt2Q7
# 3NOgrqE9Qa4iLr/qHw/ftrG+jLGgDfCxRsuhvuUFIY6lhS0hgMTMpLKk45fFAhwR
# AgMBAAE=
# -----END PUBLIC KEY-----'''

# pubkey = RSA.importKey(key_encoded)
# modulus = pubkey.n
# public_exponent = pubkey.e


import math
# from glob import glob

# p , q = 0, 0

# for filename in glob('./otherKeys/*pubkeyRSA_RW*.pem'):
#     f = open(filename)
#     key2 = f.read()
#     pubkey2 = RSA.importKey(key2)
#     modulusB = pubkey2.n
#     g = math.gcd(modulus,modulusB)
#     if g != 1:
#         if not p:
#             p = g
#         else:
#             q = g
#             break
# phi = (p-1)*(q-1)
# private_exponent = sympy.gcdex(public_exponent,phi)[0]


# from Crypto.Cipher import PKCS1_OAEP

# privateA = RSA.construct((modulus, public_exponent, int(private_exponent)))

# outputA = open('PrivateKey.pem', 'wb')
# outputA.write(privateA.exportKey('PEM'))
# outputA.close()

key = '''-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA2hTnyuijq265D/sZbmP3
5r5pPnqz73SlNocf7/DaULPHqo2EAv1XaBvuIzwqqUQ/i51vKvLCJX5jjuwCEHyk
MeJzpVlvYjc1Z+28K5wsUVCtfVNxuJY+Z/UtRMTnX9c6ruw9c2ky7tKmor1lm/Jv
Vo7rCWV7TPw9WAfFBjaH1qMxO9Fgfh0NdI2XIfgwqzXmowGp3H2ioqeqpmQPwGFq
ktkot6jm6wcfet0n00h2emkmxVys/xnpSdJfPmw1mfxCLjk/3Wbm8rW8aWKjbXx3
4nYsoMncIMONkglVHU0wQ4WwSesOu5ru78pq3jxmftYK9Vg8aRcdY/yA7iR1kJi1
9wIDAQAB
-----END PUBLIC KEY-----'''

pubkey = RSA.importKey(key)
modulus = pubkey.n
public_exponent = pubkey.e

def leng(n):
    return math.ceil(math.log2(n))

offset = -1
while offset < 0:
    offset += 1
    high = modulus >> (512*3)
    
    high -= offset
    low = modulus & (2**512-1)
    mid = (modulus & ((2**1024-1) << 512)) >> 512


    producte = (high << 512) | low
    suma = math.isqrt(mid - ((low << 512) | high) + 2*producte)
    # print(math.ceil(math.log2(producte*4)))
    # print(math.ceil(math.log2(suma**2)))
    # print(math.ceil(math.log2(abs(suma**2 - producte*4))))

    lamda = suma**2 - 4*producte
    if (lamda < 0): 
        continue
    print('si soy')
    r = (suma + math.isqrt(lamda))//2
    s = (suma - math.isqrt(lamda))//2

    p = (r << 512) | s
    q = (s << 512) | r
    if (p*q == modulus):
        print('aki toi')

