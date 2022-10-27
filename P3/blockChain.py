import math
import hashlib
import sympy
import random
from tests import run_test

d = 16
class block:
    def __init__(self):
        self.block_hash = 0
        self.previous_block_hash = 0
        self.transaction = transaction(150, rsa_key())
        self.seed = 12
    
    def genesis(self, transaction):
        self.transaction = transaction
        self.previous_block_hash = 0
        self.getBlockHash(transaction)

    def next_block(self, transaction):
        self.transaction = transaction
        self.previous_block_hash = self.block_hash
        self.getBlockHash(transaction)
    
    def verify_block(self):
        prevCheck = self.previous_block_hash < 2**(256-d)
        transCheck = self.transaction.verify()
        currCheck = self.block_hash < 2**(256-d) and self.getHash(self.seed, self.transaction) == self.block_hash
        return prevCheck and transCheck and currCheck
    
    def getBlockHash(self, transaction):
        seed = 0
        h = self.getHash(seed, transaction)
        while h >= 2**(256-d):
            seed = seed + 1
            h = self.getHash(seed, transaction)
        self.seed = seed
        self.block_hash = h

    def getHash(self, seed, transaction):
        e = str(self.previous_block_hash)
        e += str(self.transaction.public_key.publicExponent)
        e += str(self.transaction.public_key.modulus)
        e += str(self.transaction.message)
        e += str(self.transaction.signature)
        e += str(seed)
        return int(hashlib.sha256(e.encode()).hexdigest(), 16)

class block_chain:
    def __init__(self, transaction):
        self.list_of_blocks = [block().genesis(transaction)]

    def add_block(self, transaction):
        newBlock = self.list_of_blocks[-1].next_block(transaction)
        self.list_of_blocks.append(newBlock)
    
    def verify(self):
        if self.list_of_blocks[0].previous_block_hash != 0:
            return False
        for i in range(len(self.list_of_blocks)):
            if (not self.list_of_blocks[i].verify_block()):
                return False
            if i > 0 and self.list_of_blocks[i].previous_block_hash != self.list_of_blocks[i-1].block_hash:
                return False
        return True

class transaction:
    def __init__(self, message, RSAkey):
        self.public_key = rsa_public_key(RSAkey)
        self.message = message
        self.signature = RSAkey.sign(message)
    
    def verify(self):
        return self.public_key.verify(self.message, self.signature)

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
# b = block()
# bc = block_chain(t)
# b.genesis(t)
run_test(a, b, t)



# x2 + (r+s)x + rs = 0