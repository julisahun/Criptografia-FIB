from Crypto.PublicKey import RSA
import sympy

key_encoded='''-----BEGIN PUBLIC KEY-----
MIIBITANBgkqhkiG9w0BAQEFAAOCAQ4AMIIBCQKCAQByM12PLgtaKidKoXwNWXZO
6PhiNKqTU9yUYv81WkTxdn09+reugyUJ7ZIZGQAfWVszAuIgiaMb6/Dl8NRFx754
oGIMs+37xeVS36RbpAehgJuEm6SmX3NEA4liLipInux8bBlRjxZG68BA/PsVp1W0
18zkYft2bFf2FvghXdOy9UDo5s5aO+mqcwxcm2xzJhIQ916BP6I9rcfvId0mfzQg
JU/0iaLp/F8SkpPdmn2YFY7KV0P7qSX+22hsnJMZExQIPdHhs9hH9PA0qfWYt2Q7
3NOgrqE9Qa4iLr/qHw/ftrG+jLGgDfCxRsuhvuUFIY6lhS0hgMTMpLKk45fFAhwR
AgMBAAE=
-----END PUBLIC KEY-----'''

pubkey = RSA.importKey(key_encoded)
modulus = pubkey.n
public_exponent = pubkey.e


import math
from glob import glob

p , q = 0, 0

for filename in glob('./otherKeys/*pubkeyRSA_RW*.pem'):
    f = open(filename)
    key2 = f.read()
    pubkey2 = RSA.importKey(key2)
    modulusB = pubkey2.n
    g = math.gcd(modulus,modulusB)
    if g != 1:
        if not p:
            p = g
        else:
            q = g
            break
phi = (p-1)*(q-1)
private_exponent = sympy.gcdex(public_exponent,phi)[0]


from Crypto.Cipher import PKCS1_OAEP

privateA = RSA.construct((modulus, public_exponent, int(private_exponent)))

outputA = open('PrivateKey.pem', 'wb')
outputA.write(privateA.exportKey('PEM'))
outputA.close()