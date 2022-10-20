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