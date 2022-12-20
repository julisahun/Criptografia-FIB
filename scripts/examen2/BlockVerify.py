from copyreg import pickle
import math
import hashlib
import copy
import sympy
import random

d = 8
mod = 17609275718897705797693944927749287888098244670668123740639071754645310623129481163456157175152182448859534944406503550063680832132391217767945865892791446701045300663542231860126167946761334266310775875215974588540130332715652080668109605032193091094381386062991019989923988755261615483526208151537459902377091178704741629061653924653619269147925439410819658680918614713976644830989135022928100235342831933477257862730290709342557366103932579480407236923267397181905380652289162708336347529812558300142444957614597991783784594577910954543574671560060468339162220918942208119768314466039044657851139303014324171751473
e = 65537
msg = 74978285425673526727744618033707927825626444397979562261062263846703991521232
signature = 6306714462597086943864166428997195756246047584818563356624388711605293265512004643270621363757311633853686407911299042681324831062031939006448252465864316154210553408929313124594310633253211597300372011199757340195192141062673992021263319153394339390091671489462185019891530862567107337292757654243736433524940103034897680086348329193893311876271379794330527836764028061347576294800408673070408006725853291638167052717629792975737036226866898699689308998507847894294564707798890152714902931899430409016696396691053922354964984394806772752312690374469466150646983385381906139685745256122316098042154355375822111997070
prev_hash = 312242924808911849479051425103604997481886996854157223258323582102268035232
hash = 32913054361703563669153793576202057517067728388035989298541810241209692097
seed = 32913054361703563669153793576202057517067728388035989298541810241209692097

class block:
    def __init__(self, hash, prev_hash, transaction, seed):
        self.block_hash = hash
        self.previous_block_hash = prev_hash
        self.transaction = transaction
        self.seed = seed
    
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
        currCheck = self.block_hash < 2**(256-d) and self.getHash(self.seed) == self.block_hash
        if not prevCheck:
            print("Previous block hash is not less than 2^(256-d)")
        if not transCheck:
            print("Transaction is not valid")
        if not currCheck:
            print("Current block hash is not less than 2^(256-d) or does not match the hash")
        return prevCheck and transCheck and currCheck
    
    def getBlockHash(self):
        seed = 0
        h = self.getHash(seed)
        while h >= 2**(256-d):
            seed = seed + 1
            h = self.getHash(seed)
        self.seed = seed
        self.block_hash = h

    def getHash(self, seed):
        e = str(self.previous_block_hash)
        e += str(self.transaction.public_key.publicExponent)
        e += str(self.transaction.public_key.modulus)
        e += str(self.transaction.message)
        e += str(self.transaction.signature)
        e += str(seed)
        return int(hashlib.sha256(e.encode()).hexdigest(), 16)

class block_chain:
    def __init__(self, transaction):
        b = block()
        b.genesis(transaction)
        self.list_of_blocks = [b]
        

    def add_block(self, transaction): 
        newBlock = copy.deepcopy(self.list_of_blocks[-1])
        newBlock.next_block(transaction)
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
    def __init__(self, message, signature):
        self.public_key = rsa_public_key()
        self.message = message
        self.signature = signature #RSAkey.sign(message)
    
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

    def __init__(self, bits_modulo=4096, e=2**16+1):
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
        while True:

            p = random.getrandbits(bits_modulo)
            retry = 1
            while not sympy.isprime(p):
                if retry % 100 == 0:
                    print(retry)
                retry += 1
                p = random.getrandbits(bits_modulo)
            q = random.getrandbits(bits_modulo)
            while not sympy.isprime(q) or p == q:
                if retry % 100 == 0:
                    print(retry)
                retry += 1
                q = random.getrandbits(bits_modulo)
            if  math.gcd(e,p*q) == 1 and e < (p-1)*(q-1):
                print(retry)
                return int(p), int(q)

class rsa_public_key:
    def __init__(self):
        self.publicExponent = e#rsa_key.publicExponent
        self.modulus = mod#rsa_key.modulus

    def verify(self, message, signature):
        return pow(signature,self.publicExponent,self.modulus) == message



key = rsa_public_key()
t = transaction(msg, signature)
b = block(hash, prev_hash, t, seed)
print(b.verify_block())