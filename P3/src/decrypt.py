from Crypto.PublicKey import RSA
import sympy


####################### 2.1 #######################
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
name='juli.sahun'

for filename in glob('../allKeys/*pubkeyRSA_RW*.pem'):
    f = open(filename)
    if name in f.name:
        continue
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
private_exponent = sympy.mod_inverse(public_exponent,phi)


privateA = RSA.construct((modulus, public_exponent, int(private_exponent)))

outputA = open('PrivateKey.pem', 'wb')
outputA.write(privateA.exportKey('PEM'))
outputA.close()

## decrypt rsa 
#
# openssl rsautl -decrypt -inkey PrivateKey.pem -in pseudoFiles/juli.sahun_RSA_pseudo.enc -out aes.key
#
#
## decrypt aes
#
# openssl enc -d -aes-128-cbc -pbkdf2 -kfile aes.key -in pseudoFiles/juli.sahun_AES_pseudo.enc -out pic


####################### 2.2 #######################
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
b = 512

offset = -1

while offset < 5:
    offset += 1

    high = (modulus >> b*3) - offset
    mid = (modulus & ((2**(2*b)-1) << b)) >> b
    low = modulus & (2**b-1)

    producte = (high << b) | low
    suma = math.isqrt(mid - (low << b | high) + 2*producte + (offset << 2*b))


    d = suma**2 - 4*producte
    if (d < 0): 
        continue
    r = (suma + math.isqrt(d))//2
    s = (suma - math.isqrt(d))//2

    p = (r << b) | s
    q = (s << b) | r
    if (p*q == modulus):
        break


phi = (p-1)*(q-1)
private_exponent = sympy.mod_inverse(public_exponent,phi)

privateA = RSA.construct((modulus, public_exponent, int(private_exponent)))

outputA = open('PrivateKey.pem', 'wb')
outputA.write(privateA.exportKey('PEM'))
outputA.close()

