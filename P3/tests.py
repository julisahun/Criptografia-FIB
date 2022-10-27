import pickle

def signatureTest(message, signer, verifier):
    otherMessage = message + 1
    if not verifier.verify(message, signer.sign(message)) or verifier.verify(message, signer.sign(otherMessage)): 
        print('Signature test not passed')
    else:
        print('Signature test passed')

def transactionTest(transaction):
    if not transaction.verify:
        print('Transaction test not passed')
    else:
        print('Transaction test passed')
    
def testBlockChain():
    with open('./files/Cadena_bloques_valida.block', 'rb') as validData:
        validBc = pickle.load(validData)
    with open('./files/Cadena_bloques_bloque_falso.block', 'rb') as invalidData:
        invalidBc = pickle.load(invalidData)
    with open('./files/Cadena_bloques_seed_falsa.block', 'rb') as invalidData2:
        invalidBc2 = pickle.load(invalidData2)
    with open('./files/Cadena_bloques_transaccion_falsa.block', 'rb') as invalidData3:
        invalidBc3 = pickle.load(invalidData3)
    if not validBc.verify() or invalidBc.verify() or invalidBc2.verify() or invalidBc3.verify():
        print('Block chain test not passed')
    else:
        print('Block chain test passed')


def run_test(a, b, t):
    signatureTest(150, a, b)
    transactionTest(t)
    testBlockChain()
        