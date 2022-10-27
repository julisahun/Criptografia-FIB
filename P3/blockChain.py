import math
import sympy
import random
from tests import run_test

class block:
    def __init__(self):
        self.block_hash
        self.previous_block_hash
        self.transaction
        self.seed

class transaction:
    def __init__(self, message, RSAkey):
        self.public_key = rsa_public_key(RSAkey)
        self.message = message
        self.signature = RSAkey.sign(message)
    
    def verify(self):
        return self.public_key.verify(message, signature)

class rsa_key:
    def check_congruent(self,a,c,m,debug=True):
        if (a % m) != (c % m):
            print("Congruent check not passed.")
            exit(1)
        else:
            if debug:
                print("Congruent check passed.")
            return True

    def __init__(self, bits_modulo=2048, e=2**16+1):
        self.primeP, self.primeQ =  self.getPrimes(e, bits_modulo)
        self.phi = (self.primeP-1)*(self.primeQ-1)
        self.publicExponent = e
        self.privateExponent = int(sympy.gcdex(e, self.phi)[0])
        self.modulus = self.primeP*self.primeQ
        self.privateExponentModulusPhiP = int(self.privateExponent % (self.primeP-1))
        self.privateExponentModulusPhiQ = int(self.privateExponent % (self.primeQ-1))
        self.inverseQModulusP = int(sympy.mod_inverse(self.primeQ, self.primeP))

        self.check_congruent(self.privateExponent * self.publicExponent, 1, self.phi,debug=False)
        self.check_congruent(self.privateExponentModulusPhiP, self.privateExponent, self.primeP-1,debug=False)
        self.check_congruent(self.privateExponentModulusPhiQ, self.privateExponent, self.primeQ-1,debug=False)
        self.check_congruent(self.inverseQModulusP * self.primeQ, 1, self.primeP,debug=False)
    
    def sign(self, message):
        a = pow(message, self.privateExponentModulusPhiP, self.primeP)
        b = pow(message, self.privateExponentModulusPhiQ, self.primeQ)
        qq = self.inverseQModulusP * self.primeQ
        pp = 1 - qq
        return pp*b + qq*a
    
    def sign_slow(self, message):
        return pow(message, self.privateExponent, self.modulus)
    
    def verify(self, message, signature):
        return pow(signature,self.publicExponent,self.modulus) == message


    def getPrimes(self,e, bits_modulo):
        bits_modulo = bits_modulo - 1
        while True:
            p = random.randint(2**(bits_modulo/2 - 1)+1,2**(bits_modulo/2)-1)
            while not sympy.isprime(p):
                p = random.randint(2**(bits_modulo/2 - 1)+1,2**(bits_modulo/2)-1)
            q = random.randint(2**(bits_modulo/2 - 1 )+1,2**(bits_modulo/2)-1)
            while not sympy.isprime(q) or p == q:
                q = random.randint(2**(bits_modulo/2 - 1)+1,2**(bits_modulo/2)-1)
            if  math.gcd(e,p*q) == 1 and e < (p-1)*(q-1):
                return int(p), int(q)

class rsa_public_key:
    def __init__(self, rsa_key):
        self.publicExponent = rsa_key.publicExponent
        self.modulus = rsa_key.modulus

    def verify(self, message, signature):
        return pow(signature,self.publicExponent,self.modulus) == message

a = rsa_key()
b = rsa_public_key(a)
t = transaction(150, a)

run_test(a, b, t)
