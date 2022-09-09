from queue import PriorityQueue
d = {}
comparingTriple = 'THE'

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

def getMatrix(originalTriple, resultTriple):
    for row0 in rows(originalTriple, resultTriple, 0):
        for row1 in rows(originalTriple, resultTriple, 1):
            for row2 in rows(originalTriple, resultTriple, 2):
                matrix = [row0, row1, row2]
                if determinant3(matrix)%26 == 0:
                    yield matrix
def toInt(triple):
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
    if mostCommon.qsize() > 10:
        mostCommon.get()

# while not mostCommon.empty():

for matrix in getMatrix(toInt(comparingTriple), toInt(mostCommon.get()[1])):
    print(matrix)
