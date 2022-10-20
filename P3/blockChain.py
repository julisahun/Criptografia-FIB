class block:
    def __init__(self):
        self.block_hash
        self.previous_block_hash
        self.transaction
        self.seed

class transaction:
    def __init__(self):
        self.public_key
        self.RSAkey
        self.message
        self.signature

class rsa_key:
    def __init__(self, bits_modulo=2048, e=2**16+1):
        self.publicExponent
        self.privateExponent
        self.modulus
        self.primeP
        self.primeQ
        self.privateExponentModulusPhiP
        self.privateExponentModulusPhiQ
        self.inverseQModulusP

class rsa_public_key:
    def __init__(self):
        self.publicExponent
        self.modulus

from sympy import gcdex, mod_inverse
import Math

# d = gcdex(2, 1)[0]

#firma
# s = m**d % n -> pow(m, d % phi, n) 



##teorema chino
# X = x mod (p*q)
# a = x mod p
# b = x mod q
# p' = mod_inverse(p, q)
# q' = mod_inverse(q, p)
# pp' + qq' = 1
# X = p*p'*b + q*q'*a

#aplicado a la firma
# s = m**d % n     n = q*p
# a = m**(d % p-1) % p
# b = m**(d % q-1) % q    
