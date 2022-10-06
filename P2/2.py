from ast import While
from cgi import print_arguments
import functools
import numpy as np
from threading import local
import galois

m = [1,1,0,0,0,1,0,1,1]

class Poly:
    def __init__(self, params):
        self.params = params

    def toPoly(list):
        return Poly(list)

    def sum(self, poly):
        if type(poly) != Poly:
             poly = self.toPoly(poly)
        for i, val in enumerate(poly.params):
            self.params[i] = (self.params[i] + val) % 2

    def multX(self):
        self.params.append(0)
        val = self.params.pop(0)
        if val == 1:
            self.sum(Poly([1,0,0,0,1,0,1,1]))

    def mult(self,poly):
        list = []
        if type(poly) == Poly:
            list = poly.params
        else:
            list = poly
        acc = Poly([0,0,0,0,0,0,0,0])
        for indx, val in enumerate(list):
            if val == 0: continue
            original = self
            pow = 7-indx
            while pow > 0:
                original.multX()
                pow -= 1
            acc.sum(original)
        self = acc
            


    def print(self):
        print(self.params)

def polydivB2(p,q): #TODO
    r = p

    return r
    
def irreductible4():
    irreduct = []
    first = True
    for i5 in [0,1]:
        for i4 in [0,1]:
            for i3 in [0,1]:
                for i2 in [0,1]:
                    for i1 in [0,1]:
                        if first: 
                            first = False
                            continue
                        isIrr = True
                        for poly in irreduct:
                            a = np.poly1d([0,0,0,i5,i4, i3, i2, i1])
                            b = np.poly1d(poly)
                            print(a, b, np.polydiv(a,b))
                            if np.polydiv(a,b)[1][0] == 0 and np.polydiv(a,b)[0] != a:
                                isIrr = False
                                break
                        if isIrr:
                            irreduct.append([0,0,0,i5,i4, i3, i2, i1])
    return irreduct

irreduct4 = irreductible4()
print(irreduct4)
irreduct = []
for i7 in [0,1]:
    for i6 in [0,1]:
        for i5 in [0,1]:
            for i4 in [0,1]:
                for i3 in [0,1]:
                    for i2 in [0,1]:
                        for i1 in [0,1]:
                            for i0 in [0,1]:
                                a = np.poly1d([1,i7,i6,i5,i4,i3,i2,i1,i0])
                                isIrr = True    
                                for poly in irreduct4:
                                    b = np.poly1d(poly)
                                    if np.polydiv(a,b)[1][0] == 0 and np.polydiv(a,b)[0] != a:
                                        isIrr = False
                                        break
                                if isIrr:
                                    irreduct.append([1,i7,i6,i5,i4,i3,i2,i1,i0])
# print(irreduct, len(irreduct))

