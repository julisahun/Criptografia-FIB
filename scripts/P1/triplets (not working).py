import numpy as np
from sympy import comp

#no funciona

def toInt(triple):
    ret = []
    for c in triple:
        ret.append(ord(c) - ord('A'))
    return ret
def toChar(number):
    return "".join([str(i) for i in list(map(lambda x: chr((round(x) % 26)+ord('A')), number))])
def determinant3(a):
    return (a[0][0] * (a[1][1] * a[2][2] - a[2][1] * a[1][2])
           -a[1][0] * (a[0][1] * a[2][2] - a[2][1] * a[0][2])
           +a[2][0] * (a[0][1] * a[1][2] - a[1][1] * a[0][2]))
def customRound(value):
    return round(value, 4)
def toMatrix(array):
    ret = []
    for i in range(3):
        ret.append(list(map(round,[array[i*3], array[i*3+1], array[i*3+2]])))
    return ret

def translate(triple, matrix):
    a = np.array(matrix)
    b = np.array(toInt(triple))
    return toChar(a.dot(b))

def translateText(matrix, text):
    i = 0
    triple = ''
    ciphred = ''
    c = 0
    for char in text:
        if i == 3:
            ciphred += translate(triple, matrix)
            triple = ''
            i = 0
        triple += char
        i += 1
    return ciphred

def matrix(originalTriples, resultTriples):
    originalTriples = list(map(toInt, originalTriples))
    resultTriples = list(map(toInt, resultTriples))

    i0 = [originalTriples[0][0], originalTriples[0][1], originalTriples[0][2], 0, 0, 0, 0, 0, 0]
    j0 = [0, 0, 0, originalTriples[0][0], originalTriples[0][1], originalTriples[0][2], 0, 0, 0]
    k0 = [0, 0, 0, 0, 0, 0, originalTriples[0][0], originalTriples[0][1], originalTriples[0][2]]

    i1 = [originalTriples[1][0], originalTriples[1][1], originalTriples[1][2], 0, 0, 0, 0, 0, 0]
    j1 = [0, 0, 0, originalTriples[1][0], originalTriples[1][1], originalTriples[1][2], 0, 0, 0]
    k1 = [0, 0, 0, 0, 0, 0, originalTriples[1][0], originalTriples[1][1], originalTriples[1][2]]
    
    i2 = [originalTriples[2][0], originalTriples[2][1], originalTriples[2][2], 0, 0, 0, 0, 0, 0]
    j2 = [0, 0, 0, originalTriples[2][0], originalTriples[2][1], originalTriples[2][2], 0, 0, 0]
    k2 = [0, 0, 0, 0, 0, 0, originalTriples[2][0], originalTriples[2][1], originalTriples[2][2]]

    A = np.array([i0, j0, k0, i1, j1, k1, i2, j2, k2])
    B = np.array([resultTriples[0][0], resultTriples[0][1], resultTriples[0][2], 
                 resultTriples[1][0], resultTriples[1][1], resultTriples[1][2], 
                 resultTriples[2][0], resultTriples[2][1], resultTriples[2][2]])
    try:
        X = np.linalg.inv(A).dot(B)
    except:
        return None, False
    m = toMatrix(X)
    if determinant3(m) % 26 == 1: 
        return m, True
    else: return None, False

text = open('text.txt').read()
occurrences = {}
for i in range(len(text)):
    try:
        triplet = text[i] + text[i+1] + text[i+2]
        if triplet not in occurrences:
            occurrences[triplet] = 1
        else:
            occurrences[triplet] = occurrences[triplet] + 1
    except:
        break

commonTriplets = list(occurrences.keys())[0:3]

comparingTriples = ['the',
'and',
'tha',
'ent',
'ing',
'ion',
'tio',
'for',
'nde',	
'has',	
'nce',	
'edt',	
'tis',	
'oft',
'sth',
'men']
comparingTriples = list(map(lambda x: x.upper(), comparingTriples))
for a in commonTriplets:
    for b in commonTriplets:
        if a == b: continue
        for c in commonTriplets:
            if c == a or c == b: continue
            for a2 in comparingTriples:
                for b2 in comparingTriples:
                    if a2 == b2: continue
                    for c2 in comparingTriples:
                        if c2 == b2 or c2 == a2: continue
                        m, value = matrix([a,b,c],[a2,b2,c2])
                        if value:
                            try:
                                m = np.linalg.inv(m)
                            except:
                                continue
                            c = translateText(m, text)
                            print(c.count('AND'), c[0:100])
                            print()
                            print()



