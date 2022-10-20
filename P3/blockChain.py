import math
import sympy
import random

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
        self.primeP, self.primeQ =  self.getPrimes(e, bits_modulo)
        self.phi = (self.primeP-1)*(self.primeQ-1)
        self.publicExponent = e
        self.privateExponent = int(sympy.gcdex(e, self.phi)[0])
        self.modulus = self.primeP*self.primeQ
        self.privateExponentModulusPhiP = int(self.privateExponent % (self.primeP-1))
        self.privateExponentModulusPhiQ = int(self.privateExponent % (self.primeQ-1))
        self.inverseQModulusP = int(sympy.mod_inverse(self.primeQ, self.primeP))
    
    def sign(self, message):
        a = pow(message, self.privateExponentModulusPhiP, self.primeP)
        b = pow(message, self.privateExponentModulusPhiQ, self.primeQ)
        qq = self.inverseQModulusP * self.primeQ
        pp = 1 - qq
        return pp*b + qq*a
    
    def sign_slow(self, message):
        return pow(message, self.privateExponent, self.modulus)


    def getPrimes(self,e, bits_modulo):
        bits_modulo = bits_modulo - 1
        while True:
            p = random.randint(2**(bits_modulo/2 - 1)+1,2**(bits_modulo/2)-1)
            while not sympy.isprime(p):
                p = random.randint(2**(bits_modulo/2 - 1)+1,2**(bits_modulo/2)-1)
            q = random.randint(2**(bits_modulo/2 - 1 )+1,2**(bits_modulo/2)-1)
            while not sympy.isprime(q) and p == q:
                q = random.randint(2**(bits_modulo/2 - 1)+1,2**(bits_modulo/2)-1)
            if  math.gcd((p-1)*(q-1), e) == 1:
                return int(p), int(q)


class rsa_public_key:
    def __init__(self):
        self.publicExponent
        self.modulus

a = rsa_key()
print(a.sign(123) - a.sign_slow(123))

# d = gcdex(e, phi)[0]

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
