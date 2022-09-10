from queue import PriorityQueue
from unittest import result
import numpy as np
d = {}
comparingTriples = ['THE', 'AND', 'ING', 'HER', 'HAT', 'HIS', 'THA']
cripted = ''

def rows(originalTriple, resultTriple, row):
    for i in range(-10,10):
        a0 = i*originalTriple[0]
        if a0 < resultTriple[row]:
            for j in range(-10,10):
                a1 = j*originalTriple[1]
                if a0 + a1 < resultTriple[row]:
                    aux = resultTriple[row]-(a0+a1)
                    if aux%originalTriple[2] == 0:
                        a2 = aux/originalTriple[2]
                        if a2 < 10 and a2 > -10:
                            l = [i, j, a2]
                            yield l
def determinant2(matrix):
    return matrix[0][0] * matrix[0][1] - matrix[0][1]* matrix[1][1]

def determinant3(a):
    return (a[0][0] * (a[1][1] * a[2][2] - a[2][1] * a[1][2])
           -a[1][0] * (a[0][1] * a[2][2] - a[2][1] * a[0][2])
           +a[2][0] * (a[0][1] * a[1][2] - a[1][1] * a[0][2]))

def getMatrix(originalTriples, resultTriples):
    #print(originalTriples, resultTriples)
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
    X = np.linalg.inv(A).dot(B)
    
    for d in X:
        if abs(round(d,0) - d) > 0.01:
            return False
    X = toMatrix(X)
    print(X)
    print(originalTriples)
    print(resultTriples)
    exit()
    aux = np.array(X)
    inv = np.linalg.inv(aux)
    for r in inv:
        for c in r:
            if abs(round(c,0) - c) > 0.01:
                return False
    if determinant3(X)%26 == 1:
        print(X)
        return X
    else:
        return False

def toMatrix(array):
    ret = []
    for i in range(3):
        ret.append(list(map(round,[array[i*3], array[i*3+1], array[i*3+2]])))
    return ret

def toInt(triple):
    ret = []
    for c in triple:
        ret.append(ord(c) - ord('A'))
    return ret

def toChar(number):
    print(number)
    return "".join([str(i) for i in list(map(lambda x: chr(x+ord('A')), number))])

def translate(triple, matrix):
    a = np.array(matrix)
    b = np.array(toInt(triple))
    return toChar(a.dot(b))

def translateText(matrix):
    i = 0
    triple = ''
    for char in cripted:
        if i == 3:
            print(translate(triple, matrix))
            triple = ''
            i = 0
        triple += char
        i += 1



with open('text.txt') as f:
    lines = f.readlines()
    cripted = lines[0]
    i = 0
    triple = ''
    for char in cripted:
        if i == 3:
            d[triple] = d.get(triple, 0) + 1
            triple = ''
            i = 0
        triple += char
        i += 1

mostCommon = PriorityQueue()

for terna in d:
    mostCommon.put((d[terna], terna))
    if mostCommon.qsize() > 20:
        mostCommon.get()

commonList = []
while not mostCommon.empty():
    commonList.append(mostCommon.get())
print(commonList)

for triplet0 in comparingTriples:
    for triplet1 in comparingTriples:
        if triplet0 == triplet1: continue
        for triplet2 in comparingTriples: 
            if triplet2 == triplet0 or triplet2 == triplet1: continue
            t0 = triplet0
            t1 = triplet1
            t2 = triplet2
            for triplet3 in commonList:
                for triplet4 in commonList:
                    if triplet4 == triplet3: continue
                    for triplet5 in commonList:
                        if triplet5 == triplet4 or triplet5 == triplet3: continue
                        t3 = triplet3[1]
                        t4 = triplet4[1]
                        t5 = triplet5[1]
                        matrix = getMatrix([t0, t1, t2], [t3, t4, t5])
                        # matrix = [[569.0000000000019, 58.00000000000021, -247.00000000000088], [43.85714285714286, 6.0000000000000036, -19.000000000000014], [380.85714285714414, 40.000000000000135, -165.00000000000057]]
                        if matrix:
                            matrix = np.linalg.inv(matrix)
                            print(matrix)
                            translateText(matrix)
