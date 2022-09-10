from queue import PriorityQueue
from unittest import result
import numpy as np
d = {}
comparingTriples = ['THE', 'AND', 'ING', 'HER', 'HAT', 'HIS', 'THA']

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
    X = toMatrix(X)
    if determinant3(X)%1 == 0 and determinant3(X)%26 == 0:
        return X
    else:
        return False

def toMatrix(array):
    ret = []
    for i in range(3):
        ret.append([array[i*3], array[i*3+1], array[i*3+2]])
    return ret

def toInt(triple):
    print(triple)
    ret = []
    for c in triple:
        ret.append(ord(c) - ord('A'))
    return ret


with open('text.txt') as f:
    lines = f.readlines()
    i = 0
    triple = ''
    for char in lines[0]:
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

for triplet0 in commonList:
    for triplet1 in commonList:
        if triplet0 == triplet1: continue
        for triplet2 in commonList: 
            if triplet2 == triplet0 or triplet2 == triplet2: continue
            t0 = triplet0[1]
            t1 = triplet1[1]
            t2 = triplet2[1]
            matrix = getMatrix(comparingTriples[0:3], [t0, t1, t2])
            if matrix:
                print(matrix)
                print(t0, t1, t2)
                print('-----------------')
