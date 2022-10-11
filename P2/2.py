import copy

m = [1,1,0,0,0,1,0,1,1]

class Poly:
    def __init__(self, params =[0,0,0,0,0,0,0,0,0]):
        self.params = params

    def toPoly(list):
        if type(list) == Poly:
            return list
        return Poly(list)

    def add(self, poly):
        if type(poly) != Poly:
             poly = self.toPoly(poly)
        for i, val in enumerate(poly.params):
            self.params[i] = (self.params[i] + val) % 2

    def multX(self):
        self.params.append(0)
        val = self.params.pop(0)
        if val == 1:
            self.add(Poly([0,1,0,0,0,1,0,1,1]))

    def mult(self,poly):
        if type(poly) == Poly:
            list = poly.params
        else:
            list = poly
        acc = Poly([0,0,0,0,0,0,0,0,0])
        for indx, val in enumerate(list):
            if val == 0: continue
            original = copy.deepcopy(self)
            pow = 8-indx
            while pow > 0:
                original.multX()
                pow -= 1
            acc.add(original)
        self.params = acc.params
     
    def gte(self, poly):       
        for i, val in enumerate(poly.params):
            if val == 1:
                return self.params[i] >= val
            elif self.params[i] == 1:
                return True

        return True

    def lte(self, poly):
        for i, val in enumerate(poly.params):
            if self.params[i] > val:
                return False
            if self.params[i] < val:
                return True
        return True  

    def eq(self, poly):
        for indx, val in enumerate(poly.params):
            if val != self.params[indx]:
                return False
        return True

    def next(self):
        for indx, val in enumerate(self.params[::-1]):
            if val == 0:
                self.params[8-indx] = 1
                return 
            else: self.params[8-indx] = 0

    def prev(self):
        for indx, val in enumerate(self.params[::-1]):
            
            if val == 1:
                self.params[8-indx] = 0
                return 
            else: self.params[8-indx] = 1
                
    def print(self):
        print(self.params)
    
    def resized(self):
        indx = 0
        while (len(self.params) - indx) > 9 and self.params[indx] == 0:
            indx += 1
        return self.params[indx:len(self.params)]

    def mod(self):
        self.params = self.resized()
        while len(self.params) > 9:
            for i, val in enumerate(m):
                self.params[i] = (self.params[i] + val) % 2
            self.params = self.resized()

def toPoly(poly):
    if type(poly) == Poly:
        a = copy.deepcopy(Poly(poly.params))
    else:
        a = copy.deepcopy(Poly(poly))
    return a

def numToPoly(num):
    pow = 256
    poly = []
    while pow != 0:
        val = 0
        if num >= pow:
            num = num - pow
            val = 1
        poly.append(val)
        pow = pow // 2
    return poly

def polyToNum(poly):
    pow = 256
    num = 0
    for val in poly:
        if val == 1: 
            num = num + pow
            pow = pow // 2
    return num
    
def mult(poly1, poly2):
    a = toPoly(poly1)
    a.mult(poly2)
    return a

def add(poly1, poly2):
    a = toPoly(poly1)
    a.add(poly2)
    return a

def div(a, b):
    #0010
    q = Poly([0,0,0,0,0,0,0,0,1])
    while a.gte(mult(q,b)):
        q.next()
        mult(q,b).print()
    q.prev()
    if a.eq(mult(q,b)):
        return [q, Poly()]
    return [q, add(a, q)]

#Nota, Les funcions de la classe Poly, modifiquen l'objecte de la classe, 
#      Les funcions del modul, no modifiquen cap dels objectes dels parametres

# entrada: a y b elementos del cuerpo representados por enteros entre 0 y 255;
# salida: un elemento del cuerpo representado por un entero entre 0 y 255 que es el
# producto en el cuerpo de a y b calculado usando la definici´on en t´erminos de
# polinomios.
def GF_product_p(a, b):
    return polyToNum(mult(numToPoly(a), numToPoly(b)))
    

# entrada: a elemento del cuerpo representado por un entero entre 0 y 255;
# salida: True si a es generador del cuerpo, False si no lo es.
def GF_es_generador(a):
    return 0

# entrada:
# salida: dos tablas (exponencial y logaritmo), la primera tal que en la posici´on i tenga
# a = g
# i y la segunda tal que en la posici´on a tenga i tal que a = g
# i
# . (g generador
# del cuerpo finito representado por el menor entero entre 0 y 255.)
# 3
def GF_tables():
    return 0

# entrada: a y b elementos del cuerpo representados por enteros entre 0 y 255;
# salida: un elemento del cuerpo representado por un entero entre 0 y 255 que es el
# producto en el cuerpo de a y b calculado usando las tablas exponencial y
# logaritmo.
def GF_product_t(a, b):
    return 0

# entrada: a elemento del cuerpo representado por un entero entre 0 y 255;
# salida: 0 si a=0x00, in
def GF_invers(a):
    return 0




# MAIN:

a = Poly([1,0,0,0,0,0,0,1,0,1])
b = Poly([0,0,0,0,0,0,1,1,1])

a.mod()
a.print()