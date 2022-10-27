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
    

def run_test(a, b, t):
    signatureTest(150, a, b)
    transactionTest(t)

        